#!/usr/bin/env python3
"""자막 없는 raw 클립 파일을 찾아 자막을 재수집해 업데이트.

사용법:
  python3 scripts/reclip_no_sub.py
  python3 scripts/reclip_no_sub.py --dry-run   # 대상 목록만 출력
"""

import argparse
import glob
import os
import re
import subprocess
import sys
import time

BRAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BRAIN_DIR, "scripts"))

from clip_youtube import get_transcript, seconds_to_ts

SOURCE_PAT = re.compile(r'source:\s*"https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})"')


def find_no_sub_files(brain_dir: str) -> list:
    results = []
    for f in glob.glob(os.path.join(brain_dir, "raw/external/**/*.md"), recursive=True):
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        if "_자막 없음_" not in content:
            continue
        m = SOURCE_PAT.search(content)
        if m:
            results.append((f, m.group(1), content))
    return results


def update_file(fpath: str, content: str, transcript: str) -> None:
    updated = content.replace("_자막 없음_", f"## Transcript\n\n{transcript}")
    with open(fpath, "w", encoding="utf-8") as fh:
        fh.write(updated)


def main():
    parser = argparse.ArgumentParser(description="자막 없는 클립 재수집")
    parser.add_argument("--dry-run", action="store_true", help="대상 목록만 출력")
    args = parser.parse_args()

    print("자막 없는 파일 탐색 중...", flush=True)
    targets = find_no_sub_files(BRAIN_DIR)
    print(f"대상: {len(targets)}개\n", flush=True)

    if args.dry_run:
        for f, vid, _ in targets:
            print(f"{vid} | {os.path.relpath(f, BRAIN_DIR)}")
        return

    ok = skip = fail = consecutive_fail = 0

    for i, (fpath, vid_id, content) in enumerate(targets, 1):
        fname = os.path.basename(fpath)[:55]
        print(f"[{i:3d}/{len(targets)}] {vid_id} {fname}", end=" ", flush=True)

        try:
            transcript = get_transcript(vid_id)
            if transcript:
                update_file(fpath, content, transcript)
                ok += 1
                consecutive_fail = 0
                print("✓ 자막", flush=True)
            else:
                skip += 1
                consecutive_fail += 1
                print("- 자막없음", flush=True)
        except subprocess.TimeoutExpired:
            skip += 1
            consecutive_fail += 1
            print("- 타임아웃", flush=True)
        except Exception as e:
            fail += 1
            consecutive_fail += 1
            print(f"✗ {e}", flush=True)

        # 연속 10개 실패 시 IP 차단 가능성 → 60초 대기
        if consecutive_fail >= 10:
            print(f"\n⚠ 연속 {consecutive_fail}개 실패 — IP 차단 가능성. 60초 대기 후 재개...", flush=True)
            time.sleep(60)
            consecutive_fail = 0
        else:
            time.sleep(2)

    print(f"\n완료: 성공 {ok}, 자막없음 {skip}, 오류 {fail}")


if __name__ == "__main__":
    main()
