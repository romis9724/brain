---
title: RAG (Retrieval-Augmented Generation)
type: concept
tags: [rag, llm, 지식관리, spring-ai, 청킹, adaptive-chunking]
sources: [[sources/llm-wiki-카파시], [sources/spring-ai-langchain4j-rag-egovframe], [sources/adaptive-chunking-rag]]
---

# RAG — 검색 증강 생성

LLM이 질문에 답할 때 외부 문서에서 관련 청크를 검색해 컨텍스트로 활용하는 방식.
NotebookLM, ChatGPT 파일 업로드, 대부분의 문서 QA 시스템이 이 방식.

LLM의 한계(학습 시점 이후 데이터 모름, 도메인 특화 지식 부족, 환각) 및 Fine-Tuning 대비 저비용이라는 이점으로 실무에서 널리 활용.

## 작동 방식

```
질문 → 관련 청크 검색(임베딩/BM25) → LLM에 컨텍스트로 전달 → 답변 생성
```

## RAG 3단계 프로세스 (Spring AI 기준)

**1단계 — 문서 준비 (ETL Pipeline, 사전 작업)**
- Reader: PDF, Markdown, JSON 등 다양한 포맷 읽기
- Transformer(Splitter): 문서를 청크로 분할
- Writer: Embedding 생성 후 Vector Store에 저장

**2단계 — 검색 (Retrieval, 런타임)**
- 사용자 질문을 Embedding 변환
- Vector Store에서 유사도 기반 Top-K 문서 검색
- 메타데이터 필터링 가능

**3단계 — 생성 (Augmented Generation, 런타임)**
- 검색된 문서를 컨텍스트로 추가
- Query + Context를 LLM에 전달
- 컨텍스트 기반 답변 생성

## Spring AI에서의 RAG 구현

**QuestionAnswerAdvisor** (단순 RAG):
```java
ChatClient.builder(chatModel).build().prompt()
    .advisors(QuestionAnswerAdvisor.builder(vectorStore).build())
    .user(question).call().content();
```

**RetrievalAugmentationAdvisor** (모듈형 RAG — 단계별 커스텀):
```java
Advisor ragAdvisor = RetrievalAugmentationAdvisor.builder()
    .queryTransformers(RewriteQueryTransformer.builder()...) // 쿼리 재작성
    .documentRetriever(VectorStoreDocumentRetriever.builder()
        .similarityThreshold(0.50).vectorStore(vectorStore).build())
    .build();
```

쿼리 변환 옵션:
- `RewriteQueryTransformer`: 모호한 쿼리를 LLM으로 재작성
- `CompressionQueryTransformer`: 대화 맥락 참조해 독립 쿼리로 압축
- `TranslationQueryTransformer`: 다국어 쿼리 번역

## LLM Wiki와의 비교

| 측면 | RAG | LLM Wiki |
|------|-----|----------|
| 지식 처리 시점 | 질문 시점 (매번) | 수집 시점 (한 번) |
| 축적 | 없음 | 복리 |
| 인프라 | 임베딩 DB 필요 | 마크다운 파일만 |
| 복잡한 합성 | 5개 문서 매번 재조각 | 이미 통합된 페이지 |
| 모순 처리 | 매번 재발견 | 플래그 후 유지 |

## 한계

- **축적 없음**: 같은 질문을 반복해도 지식이 쌓이지 않음
- **합성 한계**: 여러 문서에 걸친 미묘한 연결은 매번 재발견해야 함
- **RAG 인프라**: 임베딩 모델, 벡터 DB 등 별도 인프라 필요

## LLM Wiki에서의 대안

index.md를 통한 카탈로그 기반 내비게이션.
소규모(~100개 소스, 수백 페이지)에서는 임베딩 RAG 없이도 충분히 동작.
대규모에서는 qmd([[entities/tools/qmd]]) 같은 로컬 검색 엔진으로 확장.

## Adaptive Chunking — 청킹 최적화 (LREC 2026)

기존 청킹 방식의 공통 한계: **모든 문서에 하나의 전략 강제**. Ekimetrics 연구팀이 제안한 Adaptive Chunking은 문서별로 최적 청킹 방법을 자동 선택한다.

**5가지 내재적 품질 지표** (정답 없이 계산):
- RC: 개체-대명사 쌍이 같은 청크 안에 보존되는 비율
- BI: 단락·표 등 구조 블록 무결성
- ICC: 청크 내 문장들의 의미 응집성
- DCC: 청크와 주변 컨텍스트 윈도우의 의미 일관성
- SC: 100~1,100 토큰 범위 준수 비율

**성능**: RAG 종합 성능 62% → 72%, 답변 가능 질문 49개 → 65개. 내재적 지표 0.4~2.4pp 차이가 RAG 성능 8~10pp 차이로 **증폭**.

**실용 원칙**: 항상 크기 정규화(후처리)할 것. 단일 지표 최적화 금지. → [[sources/adaptive-chunking-rag]]

## 연결

- [[concepts/llm-wiki]] — RAG의 한계를 극복하는 패턴
- [[concepts/spring-ai]] — Spring AI에서의 RAG 구현 상세
- [[concepts/langchain4j]] — Langchain4j에서의 RAG 구현
- [[sources/adaptive-chunking-rag]] — Adaptive Chunking 논문 상세
