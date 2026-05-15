---
title: qmd
type: entity
subtype: tool
tags: [검색, 마크다운, cli, mcp]
related: [[concepts/llm-wiki]]
---

# qmd

마크다운 파일을 위한 로컬 검색 엔진. [[concepts/llm-wiki]] 패턴의 선택적 확장 도구.

## 특징

- **하이브리드 검색**: BM25 + 벡터 검색 + LLM 리랭킹
- **완전 온디바이스**: 외부 서버 없이 로컬 실행
- **CLI + MCP 서버**: LLM이 shell 또는 MCP 도구로 직접 호출 가능
- GitHub: `tobi/qmd`

## LLM Wiki에서의 역할

wiki가 수백 페이지 이상으로 커졌을 때 index.md 기반 내비게이션의 한계를 보완.
LLM이 CLI로 `qmd search "키워드"` 형태로 관련 페이지를 효율적으로 탐색.

소규모(~100 소스)에서는 index.md로 충분. 대규모에서 도입 고려.

## 연결

- [[concepts/llm-wiki]] — 대규모 wiki 검색 확장
- [[concepts/rag]] — qmd는 경량 로컬 RAG 역할을 함
