---
title: NotebookLM
type: entity
subtype: tool
tags: [google, 리서치, ai-tool]
---

# NotebookLM

Google의 AI 기반 리서치 도구. 소스 문서를 기반으로 깊이 있는 조사·요약·분석을 제공.

## 특징

- 소스 기반 답변 (RAG 방식)
- 웹 브라우저 UI 기본 제공
- Python 라이브러리(`notebooklm-py`)로 CLI 사용 가능

## LLM Wiki와의 조합

[[sources/notebooklm-cli-llm위키-튜토리얼]]에서 소개된 워크플로우:
- NotebookLM이 리서치 엔진 역할 (깊이 있는 웹 조사)
- Playwright로 CLI에서 제어 → 토큰 절약
- 조사 결과를 Hermes Agent([[entities/tools/hermes-agent]])가 받아서 LLM Wiki 형식으로 저장

## 관련 리소스

- GitHub: `teng-lin/notebooklm-py`
- 연동 플로우: `reallygood83/notebooklm-llm-wiki-flow`

## 연결

- [[concepts/llm-wiki]] — 조사 결과를 저장하는 패턴
- [[entities/tools/hermes-agent]] — LLM Wiki 처리 담당 에이전트
