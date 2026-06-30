---
title: PKM (Personal Knowledge Management)
type: concept
tags: [pkm, 지식관리, 세컨드브레인, 제텔카스텐, dikw]
sources: [[sources/옵시디언-주식분석-llm위키]], [[sources/세컨드브레인-제텔카스텐-개론]]
---

# PKM — 개인 지식 관리

개인이 수집·처리·저장·검색·공유하는 지식을 체계적으로 관리하는 방법론의 총칭.

## 주요 프레임워크 비교

| 프레임워크 | 제안자 | 관리 주체 | 핵심 구조 |
|------------|--------|-----------|-----------|
| PARA | Tiago Forte | 사람 | Projects, Areas, Resources, Archive |
| ACE | Nick Milo | 사람 | Atlas, Calendar, Extras |
| 세컨드 브레인 | Tiago Forte | 사람 | 수집→정리→추출→표현 (CODE) |
| 제텔카스텐 | Niklas Luhmann | 사람 | 원자적 노트 + 메모 간 연결 |
| **LLM Wiki** | **Andrej Karpathy** | **LLM** | Raw → Wiki → Schema |

## DIKW 위계 — 지식이 가치가 되는 단계

**Data → Information → Knowledge → Wisdom/Action → Value**

데이터에서 패턴을 발견하면 Information, 나에게 의미를 부여하면 Knowledge, Knowledge로 액션(글·논문 출판)을 취할 때 비로소 Value가 발생. 세컨드 브레인·제텔카스텐 모두 "기록 → 미래의 나에게 가치 축적"이라는 같은 원리.

## 연구자 워크플로우 (옵시디언 중심)

검색(Google Scholar·Publish or Perish) → 수집([[entities/tools/zotero|Zotero]]) → 읽기·하이라이트(AI 보조) → 노트(옵시디언 허브) → 집필(매뉴스크립트 → Pandoc 워드 내보내기) → 다시 리서치로 회귀하는 반복 루프. 노션의 한계 때문에 연구자에게는 옵시디언이 권장된다.

## LLM Wiki의 PKM적 의의

기존 PKM은 **사람이 분류·관리·업데이트** 해야 함 → 끈기·맥락 유지 실패 시 지식 휘발.
LLM Wiki는 **LLM이 모든 유지보수**를 담당 → 사람은 원본 자료 제공과 질문에 집중.

단, 개인적 경험·일기 등 정확성이 중요한 기록은 사람이 직접 관리하는 것이 적합.

## 연결

- [[concepts/llm-wiki]] — LLM이 유지하는 PKM 패턴
- [[concepts/제텔카스텐]] — 메모 연결 중심의 구체적 방법론
- [[sources/옵시디언-주식분석-llm위키]] — PARA·ACE·LLM Wiki 비교 맥락
- [[sources/세컨드브레인-제텔카스텐-개론]] — 세컨드 브레인·DIKW·연구자 워크플로우
