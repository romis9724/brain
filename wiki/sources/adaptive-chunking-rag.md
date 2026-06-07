---
title: Adaptive Chunking — RAG 문서마다 최적 청킹 자동 선택 프레임워크
type: source
date: 2026-06-03
source_file: raw/Adaptive Chunking RAG 문서마다 최적의 청킹 전략을 자동 선택하는 프레임워크.md
tags: [rag, 청킹, adaptive-chunking, ai논문, ekimetrics, lrec2026]
---

# Adaptive Chunking — RAG 문서마다 최적 청킹 자동 선택

Ekimetrics(Paulo Roberto de Moura Junior, Jean Lelong, Annabelle Blangero) 연구팀이 제안한 RAG 청킹 최적화 프레임워크. LREC 2026 채택 논문. "모든 문서에 하나의 청킹 전략을 쓰는 one-size-fits-all 방식은 존재하지 않는다"는 핵심 주장.

## 요약

RAG 성능의 숨은 병목인 청킹 단계를 정면으로 다루는 논문. 5가지 내재적 품질 지표를 정의하고, 이 지표로 각 문서에 최적인 청킹 방법을 자동 선택하는 Adaptive 정책을 제안. 모델이나 프롬프트를 전혀 바꾸지 않고도 RAG 종합 성능을 62% → 72%로 끌어올리고, 답변 가능한 질문 수를 49개 → 65개로 늘렸다.

## 핵심 포인트

### 왜 청킹이 RAG의 숨은 병목인가
- 청크 경계가 맥락을 끊으면 검색이 불완전해짐 → "맥락 보존 딜레마"
- 기존 평가 방식(Hits@k, Recall@K 등)은 청킹 자체의 효과를 분리하지 못함
- LLM 컨텍스트 창이 커져도 효율적 검색을 위해 청킹은 여전히 결정적

### 기존 청킹 방식의 한계
| 방식 | 한계 |
|------|------|
| 문장 기반 분할 | 단락 등 더 큰 논리 블록을 끊음 |
| 재귀적 분할 (LangChain) | 길이만 맞추다 서로 무관한 주제가 한 청크에 |
| 의미 기반 청킹 | 응집성은 좋으나 임베딩 반복 계산 비용 과다 |
| LLM 기반 분할 | 단일 전략 가정 + 높은 오버헤드 |

### 5가지 내재적 지표 (정답 없이 계산 가능)
| 지표 | 측정 내용 |
|------|----------|
| RC (References Completeness) | 개체-대명사 쌍이 같은 청크 안에 보존되는 비율 |
| BI (Block Integrity) | 단락·표·그림 등 구조 블록이 끊기지 않는 비율 |
| ICC (Intrachunk Cohesion) | 청크 내 문장들의 의미적 응집성 |
| DCC (Document Contextual Coherence) | 청크와 주변 슬라이딩 윈도우의 의미 일관성 |
| SC (Size Compliance) | 100~1,100 토큰 범위 준수 비율 |

다섯 지표 간 상관계수 -0.44 < ρ < 0.31 → 서로 보완적 현상 측정. ICC↑ vs DCC↓, ICC↑ vs BI↓ 등 상충 관계가 단일 지표 최적화 대신 다중 지표 + 문서별 선택을 정당화.

### 두 가지 새로운 청커
- **LLM Regex Splitter**: LLM이 문서 앞부분을 보고 최적 정규식 패턴을 생성 → 나머지에 적용. 유연함 + 결정론적 분할
- **Split-then-Merge Recursive Splitter**: 1차 패스(재귀 분할) + 2차 패스(인접 조각 탐욕적 병합). 크기 준수·맥락 보존 동시 개선

**후처리 효과**: 과소·과대 청크 정규화만으로 SC와 평균 내재적 점수를 6~16pp 향상.

### 성능 결과

청킹 방법별 평균 내재적 점수:
| 방법 | 평균 |
|------|------|
| **Adaptive Chunking** | **91.07** |
| LLM regex (GPT) | 89.80 |
| LangChain recursive | 88.62 |
| Semantic | 76.49 |
| Sentence | 73.26 |

RAG 다운스트림 성능:
| 지표 | Adaptive | LangChain 기본 |
|------|----------|---------------|
| Retrieval Completeness | **67.68%** | 58.08% |
| Answer Correctness | **78.01%** | 70.11% |
| 답변한 질문 수 | **65/99** | 49/99 |

**증폭 효과**: 내재적 지표 0.4~2.4pp 차이 → RAG 성능 8~10pp 차이로 증폭됨.

### 실용적 제언
1. 전역 기본값보다 문서 인식 선택 우선 (단일 청커가 평균 최고여도 Adaptive가 우월)
2. 항상 크기를 정규화 (과소·과대 청크 후처리)
3. 응집성(ICC)과 맥락(DCC)의 균형 — 단일 지표 최적화 금지

## 한계
- RC는 Maverick 상호참조 해소 모델로 계산 → 영어 문서만 지원
- 청크 크기·슬라이딩 윈도우 크기 하이퍼파라미터가 경험적
- 청킹 전략은 색인 시점 고정 → 질의 특성에 적응하지 않음

## 관련 링크
- [[wiki/concepts/rag]] — RAG 기본 개념 및 구현
- [GitHub: ekimetrics/adaptive-chunking](https://github.com/ekimetrics/adaptive-chunking)
- [arXiv: 2603.25333](https://arxiv.org/abs/2603.25333)
