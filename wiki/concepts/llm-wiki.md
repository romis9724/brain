---
title: LLM Wiki
type: concept
tags: [llm-wiki, 지식관리, 세컨드브레인, 핵심개념]
sources: [[sources/llm-wiki-카파시]], [[sources/notebooklm-cli-llm위키-튜토리얼]], [[sources/옵시디언-주식분석-llm위키]]
---

# LLM Wiki

[[entities/people/안드레이-카파시]]가 제안한 LLM 기반 개인 지식 베이스 구축 패턴.
LLM이 지식을 매번 재발견하는 대신, **영구적으로 축적되는 wiki를 직접 작성·유지**한다.

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## RAG와의 결정적 차이

| | RAG | LLM Wiki |
|--|-----|----------|
| 지식 처리 | 질문마다 원본에서 재발견 | 한 번 컴파일 후 최신 상태 유지 |
| 축적 | 없음 | 복리로 증가 |
| 크로스 레퍼런스 | 매번 재구성 | 이미 구성됨 |
| 모순 감지 | 매번 재발견 | 한 번 플래그, 지속 반영 |

→ 자세한 비교: [[concepts/rag]]

## 3계층 구조

```
Raw sources (불변) → Wiki (LLM 작성) → Schema (CLAUDE.md)
```

- **Raw**: 원본 자료. LLM이 읽기만 함. 절대 수정 금지
- **Wiki**: LLM이 생성·유지하는 마크다운 페이지들
- **Schema**: LLM에게 wiki 구조와 워크플로우를 알려주는 지침서

## 3가지 오퍼레이션

### Ingest
새 자료를 raw/에 넣고 LLM에게 처리 요청.
하나의 자료가 10-15개 wiki 페이지에 영향을 줄 수 있음.

### Query
wiki를 기반으로 질문에 답변. index.md 먼저 읽어 관련 페이지 탐색.
**좋은 답변은 wiki 페이지로 저장** → 탐색 자체가 지식 축적.

### Lint
wiki 건강 검진. 모순, 오래된 정보, 고아 페이지, 누락 크로스 레퍼런스 점검.

## 왜 작동하는가

지식 베이스의 부담은 독서나 사고가 아니라 **북키핑(bookkeeping)** 에 있음.
LLM은 크로스 레퍼런스 업데이트를 잊지 않고, 지루해하지 않으며, 한 번에 15개 파일을 수정 가능.
유지 비용이 거의 0에 수렴하기 때문에 wiki가 살아있을 수 있음.

## 이 브레인에서의 구현

- `raw/` → Raw sources
- `wiki/` → LLM-generated wiki
- `CLAUDE.md` → Schema
- `index.md`, `log.md` → 내비게이션·이력 관리

## 실전 사례

- [[sources/notebooklm-cli-llm위키-튜토리얼]] — NotebookLM CLI 연동
- [[sources/옵시디언-주식분석-llm위키]] — 국내 주식 분석 적용
