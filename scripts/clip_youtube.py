#!/usr/bin/env python3
"""YouTube 채널/영상 → Obsidian 클립핑 스크립트

사용법:
  python3 clip_youtube.py                          # 기본값(김영익 채널)
  python3 clip_youtube.py --url <채널URL>          # 다른 채널
  python3 clip_youtube.py --url <영상URL>          # 단일 영상
  python3 clip_youtube.py --output <디렉토리>      # 저장 위치 지정
  python3 clip_youtube.py --channel <채널명>       # 채널명 override
"""

import argparse
import json
import subprocess
import os
import re
import sys
import tempfile
import time
from datetime import datetime
from typing import Optional

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("필요 패키지 설치: pip3 install youtube-transcript-api")
    sys.exit(1)

BRAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_URL = "https://www.youtube.com/@김영익/videos"
TODAY = datetime.now().strftime("%Y-%m-%d")


def parse_args():
    parser = argparse.ArgumentParser(description="YouTube → Obsidian 클립퍼")
    parser.add_argument("--url", default=DEFAULT_URL, help="YouTube 채널 또는 영상 URL")
    parser.add_argument("--output", default=None, help="저장 디렉토리 (미지정 시 자동 결정)")
    parser.add_argument("--channel", default=None, help="채널명 override")
    return parser.parse_args()


def extract_channel_name(url: str) -> str:
    """URL에서 채널명 추출"""
    m = re.search(r'@([^/\s]+)', url)
    if m:
        return m.group(1)
    m = re.search(r'/c/([^/\s]+)', url)
    if m:
        return m.group(1)
    m = re.search(r'/channel/([^/\s]+)', url)
    if m:
        return m.group(1)[:20]
    return "youtube"


def seconds_to_ts(sec: float) -> str:
    m = int(sec // 60)
    s = int(sec % 60)
    return f"{m}:{s:02d}"


def sanitize(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '', name)
    name = name.strip().strip('.')
    return name[:120] or "untitled"


def format_date(d: str) -> str:
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if d and len(d) == 8 else ""


def _segs_to_text(segs) -> Optional[str]:
    lines = []
    for s in segs:
        txt = s.text.strip().replace('\n', ' ')
        if txt:
            lines.append(f"**{seconds_to_ts(s.start)}** · {txt}")
    return '\n\n'.join(lines) if lines else None


def _parse_json3(fpath: str) -> Optional[str]:
    """yt-dlp JSON3 자막 파일 → 타임스탬프 텍스트"""
    try:
        with open(fpath, encoding="utf-8") as f:
            data = json.load(f)
        lines = []
        for event in data.get("events", []):
            segs = event.get("segs", [])
            if not segs:
                continue
            text = "".join(s.get("utf8", "") for s in segs).strip().replace('\n', ' ')
            if not text or text == "\n":
                continue
            ts = seconds_to_ts(event.get("tStartMs", 0) / 1000)
            lines.append(f"**{ts}** · {text}")
        return '\n\n'.join(lines) if lines else None
    except Exception:
        return None


def _get_transcript_ytdlp(vid_id: str) -> Optional[str]:
    """yt-dlp + Chrome 쿠키로 자동생성 자막 다운로드 (IP 차단 우회)"""
    url = f"https://www.youtube.com/watch?v={vid_id}"
    with tempfile.TemporaryDirectory() as tmpdir:
        out_tmpl = os.path.join(tmpdir, "%(id)s")
        base_cmd = ["yt-dlp", "--cookies-from-browser", "chrome",
                    "--skip-download", "--write-auto-sub",
                    "--sub-lang", "ko", "--sub-format", "json3",
                    "--output", out_tmpl]
        # curl-cffi가 있으면 브라우저 핑거프린트 우회 시도
        for cmd in [base_cmd + ["--impersonate", "chrome", url],
                    base_cmd + [url]]:
            subprocess.run(cmd, capture_output=True, text=True)
            for fname in os.listdir(tmpdir):
                if fname.endswith(".json3"):
                    return _parse_json3(os.path.join(tmpdir, fname))
    return None


def get_transcript(vid_id: str) -> Optional[str]:
    api = YouTubeTranscriptApi()

    # 1. youtube-transcript-api: 언어 선호순
    for langs in [['ko'], ['ko', 'en']]:
        try:
            result = _segs_to_text(api.fetch(vid_id, languages=langs))
            if result:
                return result
        except Exception:
            continue

    # 2. youtube-transcript-api: 자동생성 포함 전체 목록
    try:
        for t in api.list(vid_id):
            try:
                result = _segs_to_text(t.fetch())
                if result:
                    return result
            except Exception:
                continue
    except Exception:
        pass

    # 3. yt-dlp + Chrome 쿠키 폴백 (IP 차단 시)
    return _get_transcript_ytdlp(vid_id)


def make_clip(vid_id: str, title: str, upload_date: str,
              author: str, description: str = ""):  # -> tuple[str, bool]
    url = f"https://www.youtube.com/watch?v={vid_id}"
    pub = format_date(upload_date) if upload_date and upload_date != 'NA' else ""
    desc_safe = (description or "").replace('"', "'").replace('\n', ' ')[:300]
    author_tag = f"[[{author}]]" if author else ""

    transcript = get_transcript(vid_id)

    content = f"""---
title: "{title}"
source: "{url}"
author:
  - "{author_tag}"
published: {pub}
created: {TODAY}
description: "{desc_safe}"
tags:
  - "clippings"
---

![]({url})

"""
    if transcript:
        content += f"## Transcript\n\n{transcript}\n"
    else:
        content += "_자막 없음_\n"

    return content, transcript is not None


def build_seen_ids(brain_dir: str) -> dict:
    """raw/ 및 wiki/ 전체를 스캔해 YouTube 영상 ID → 발견 경로 매핑 반환.

    frontmatter의 source: 필드 또는 본문에서 YouTube 영상 ID(11자)를 추출한다.
    중복 수집 방지를 위해 실제 처리 전에 한 번만 호출한다.
    """
    seen = {}
    yt_pat = re.compile(r'(?:youtube\.com/watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})')
    for search_dir in ("raw", "wiki"):
        dir_path = os.path.join(brain_dir, search_dir)
        if not os.path.isdir(dir_path):
            continue
        for root, _, files in os.walk(dir_path):
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, encoding="utf-8") as f:
                        head = f.read(2000)  # frontmatter만 읽으면 충분
                    for m in yt_pat.finditer(head):
                        vid = m.group(1)
                        if vid not in seen:
                            seen[vid] = os.path.relpath(fpath, brain_dir)
                except Exception:
                    pass
    return seen


def get_video_list(url: str) -> list:
    """채널에서 영상 목록 반환: [(vid_id, title, upload_date), ...]"""
    result = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--print",
         "%(id)s\t%(title)s\t%(upload_date)s", url],
        capture_output=True, text=True
    )
    videos = []
    for line in result.stdout.strip().split('\n'):
        parts = line.split('\t')
        if len(parts) >= 2:
            vid_id = parts[0].strip()
            title  = parts[1].strip()
            date   = parts[2].strip() if len(parts) > 2 else ""
            if vid_id:
                videos.append((vid_id, title, date))
    return videos


def is_single_video(url: str) -> bool:
    return "watch?v=" in url or "youtu.be/" in url


def get_single_video_info(url: str) -> tuple:
    result = subprocess.run(
        ["yt-dlp", "--print", "%(id)s\t%(title)s\t%(upload_date)s",
         "--no-playlist", url],
        capture_output=True, text=True
    )
    parts = result.stdout.strip().split('\t')
    if len(parts) >= 2:
        return parts[0].strip(), parts[1].strip(), parts[2].strip() if len(parts) > 2 else ""
    return "", "", ""


def main():
    args = parse_args()

    # 채널명 결정
    channel = args.channel or extract_channel_name(args.url)

    # 출력 디렉토리 결정
    output_dir = args.output or os.path.join(BRAIN_DIR, "raw", "external", channel)
    os.makedirs(output_dir, exist_ok=True)

    print(f"채널명: {channel}")
    print(f"URL: {args.url}")
    print(f"저장위치: {output_dir}\n")

    # 영상 목록 수집
    if is_single_video(args.url):
        vid_id, title, date = get_single_video_info(args.url)
        if not vid_id:
            print("영상 정보를 가져올 수 없습니다.")
            sys.exit(1)
        videos = [(vid_id, title, date)]
    else:
        print("채널 영상 목록 수집 중...", flush=True)
        videos = get_video_list(args.url)
        print(f"총 {len(videos)}개 영상 발견", flush=True)

    # raw/ + wiki/ 전체에서 이미 수집된 영상 ID 목록 구성
    print("중복 검사 중 (raw/ + wiki/ 스캔)...", flush=True)
    seen_ids = build_seen_ids(BRAIN_DIR)
    print(f"기존 수집 영상: {len(seen_ids)}개\n", flush=True)

    # 각 영상 처리
    ok = skip = fail = 0

    for i, (vid_id, title, date) in enumerate(videos, 1):
        # 1) 영상 ID 기준 중복 체크 (raw/ 또는 wiki/ 어디에든 있으면 스킵)
        if vid_id in seen_ids:
            skip += 1
            loc = seen_ids[vid_id]
            print(f"[{i:3d}/{len(videos)}] SKIP  {title[:45]} ({loc})", flush=True)
            continue

        # 2) 파일명 기준 중복 체크 (ID 못 찾은 경우 보조 수단)
        fname = os.path.join(output_dir, f"{sanitize(title)}.md")
        if os.path.exists(fname):
            skip += 1
            print(f"[{i:3d}/{len(videos)}] SKIP  {title[:55]} (파일명 중복)", flush=True)
            continue

        print(f"[{i:3d}/{len(videos)}] 처리  {title[:55]}", end=" ", flush=True)

        try:
            content, has_tr = make_clip(vid_id, title, date, channel)
            with open(fname, "w", encoding="utf-8") as f:
                f.write(content)
            seen_ids[vid_id] = os.path.relpath(fname, BRAIN_DIR)  # 즉시 등록
            ok += 1
            print(f"{'✓ 자막' if has_tr else '✓ 메타'}", flush=True)
        except Exception as e:
            fail += 1
            print(f"✗ {e}", flush=True)

        time.sleep(0.3)

    print(f"\n완료: 성공 {ok}, 스킵 {skip}, 실패 {fail}")
    print(f"저장위치: {output_dir}")


if __name__ == "__main__":
    main()
