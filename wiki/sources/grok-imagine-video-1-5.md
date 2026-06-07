---
title: Grok Imagine Video 1.5 완전 가이드 — Aurora 엔진·프롬프트·가격
type: source
date: 2026-06-04
source_file: raw/화장품/Grok Imagine Video 1.5 완전 가이드 – Aurora 엔진·프롬프트·가격 총정리.md
tags: [ai-영상생성, grok, xai, aurora-moe, 비디오생성, 프롬프트]
---

# Grok Imagine Video 1.5 완전 가이드

xAI(Elon Musk)가 Aurora MoE 엔진으로 개발한 AI 영상 생성 모델. 2026년 5월 31일 v1.5 업그레이드. Arena.ai I2V 리더보드 1위, 경쟁 대비 최대 7배 저렴한 단가, 네이티브 오디오 통합이 차별점.

## 요약

RAG나 코딩 AI와 달리 창작·마케팅 영역 도구. 720p 해상도 제한과 15초 길이 한계가 있으나, 빠른 생성속도(30초)·네이티브 오디오·낮은 가격으로 개인 크리에이터·스타트업에 특히 유리. 프롬프트 구조화가 품질을 결정함.

## 핵심 스펙

| 항목 | 사양 |
|------|------|
| 엔진 | Aurora MoE (Autoregressive Mixture-of-Experts) |
| 해상도 | 480p / 720p |
| 프레임레이트 | 24fps |
| 영상 길이 | 1~15초 |
| 종횡비 | 7가지 (16:9, 9:16, 1:1 등) |
| 생성 속도 | 평균 약 30초 |
| 학습 인프라 | Colossus 슈퍼컴퓨터 + NVIDIA GB200 GPU 11만 대 |

## 6가지 생성 모드
1. **텍스트 → 영상 (T2V)**: 프롬프트만으로 클립 생성
2. **이미지 → 영상 (I2V)**: 정지 이미지에 동작 부여
3. **레퍼런스 → 영상**: 특정 인물·제품 기준 일관된 캐릭터 생성
4. **영상 편집**: 기존 클립 스타일·요소 수정
5. **영상 연장 (Extend Video)**: 클립 끝에서 이어지는 새 씬 자동 생성
6. **오디오 통합 생성**: 대사·배경음·효과음을 단일 패스로 동시 출력

## 강점
- **Arena.ai I2V 리더보드 1위**: ByteDance Seedance 2.0, Google Veo 상회. v1.0 대비 +52 Elo 포인트
- **네이티브 오디오**: 영상-오디오 동기화를 모델 내부에서 처리 (후반 작업 최소화)
- **가격 경쟁력**: 경쟁 대비 최대 7배 저렴
- **빠른 생성**: 30초 내 완성, 콜드 스타트 없음
- **캐릭터 일관성**: 레퍼런스 이미지 기반 동일 인물 여러 클립 생성 가능

## 약점
- 최대 720p (1080p·4K 불가) → 전문 프로덕션 부적합
- 최대 15초 → 장편 불가 (연장 기능으로 우회하나 씬 전환 품질 불일정)
- 정밀 카메라 제어 한계 (Runway Gen-4 등 대비)
- 복잡한 프롬프트(3개 이상 독립 요소)에서 환각 발생 가능
- 제품 드리프트: 카메라 이동 시 제품 형태 변형

## 프롬프트 작성법

**기본 구조**:
```
[피사체 묘사] + [카메라 움직임] + [조명/시간대] + [분위기/스타일] + [오디오 요소]
```

**예시 — 인물 클로즈업 (SNS 숏폼)**:
```
A Korean woman in a white linen dress, slow dolly-in, golden hour backlight,
soft bokeh, ambient café noise and light jazz in the background
```

**예시 — 제품 광고 (전자제품)**:
```
A sleek black smartwatch rotating on a marble surface, slow 360-degree orbit,
studio three-point lighting, no background music, subtle mechanical click sound
```

## 실용 팁
- **비용 최적화**: 초안 480p → 최종본만 720p (40~50% 절감)
- **다중 요소 제한**: 핵심 요소 3~4개로 제한, 나머지 후편집
- **제품 드리프트 방지**: 카메라 이동 "slow" 또는 "very slow" 명시
- **오디오 불필요 시**: "no background music, silent" 명시

## 관련 링크
- [[wiki/concepts/ai-도구]] — AI 영상·이미지 생성 도구 전반
