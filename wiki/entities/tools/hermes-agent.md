---
title: Hermes Agent (에르메스 에이전트)
type: entity
subtype: tool
tags: [agent-cli, llm-wiki, 자동화]
---

# Hermes Agent (에르메스 에이전트)

LLM Wiki 스킬이 내장된 에이전트 CLI. NotebookLM과 연동해 조사 결과를 자동으로 wiki로 변환.

## 특징

- **LLM Wiki 스킬 내장**: 업데이트 시 기본 스킬로 제공
- **NotebookLM CLI 연동**: Playwright를 통해 NotebookLM 브라우저를 CLI에서 제어
- **명령어 기반 워크플로우**: 커스텀 명령어(예: `notewiki`) 생성 가능
- 텔레그램 봇으로도 사용 가능

## Claude Code와의 관계

[[sources/notebooklm-cli-llm위키-튜토리얼]]에서 언급:
- Hermes Agent, Claude Code, OpenCode, Codex 모두 동일 패턴으로 동작 가능
- 이 브레인(`romis9724/brain`)은 Claude Code 기반으로 구현

## 관련 리소스

- `reallygood83/notebooklm-llm-wiki-flow` — NotebookLM 연동 플로우 GitHub 레포

## 연결

- [[concepts/llm-wiki]] — 구현하는 패턴
- [[entities/tools/notebooklm]] — 연동 리서치 도구
