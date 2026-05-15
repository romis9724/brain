---
title: RAG (Retrieval-Augmented Generation)
type: concept
tags: [rag, llm, 지식관리]
related: [[concepts/llm-wiki]], [[concepts/pkm]]
sources: [[sources/llm-wiki-카파시]]
---

# RAG — 검색 증강 생성

LLM이 질문에 답할 때 외부 문서에서 관련 청크를 검색해 컨텍스트로 활용하는 방식.
NotebookLM, ChatGPT 파일 업로드, 대부분의 문서 QA 시스템이 이 방식.

## 작동 방식

```
질문 → 관련 청크 검색(임베딩/BM25) → LLM에 컨텍스트로 전달 → 답변 생성
```

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

## 연결

- [[concepts/llm-wiki]] — RAG의 한계를 극복하는 패턴
