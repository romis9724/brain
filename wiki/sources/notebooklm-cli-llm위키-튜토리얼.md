---
title: NotebookLM을 CLI로 쓴다고? 카파시 LLM위키 + 옵시디언으로 AI 지식창고 자동 구축 완벽 튜토리얼
type: source
date: 2026-05-15
source_file: raw/external/NotebookLM을 CLI로 쓴다고? 카파시 LLM위키 + 옵시디언으로 AI 지식창고 자동 구축 완벽 튜토리얼.md
origin: https://www.youtube.com/watch?v=UUNgWvVoT4E
author: 배움의 달인 (AI·자동화)
published: 2026-04-17
tags: [llm-wiki, notebooklm, 옵시디언, hermes-agent, 자동화]
---

# NotebookLM CLI + LLM Wiki + 옵시디언 튜토리얼

## 한 줄 요약

Hermes Agent CLI에서 NotebookLM을 Playwright로 연동해 조사 결과를 자동으로 LLM Wiki 형식(위키링크)으로 옵시디언에 저장하는 워크플로우.

## 핵심 포인트

- **핵심 조합**: NotebookLM(조사) + Hermes Agent CLI(처리) + LLM Wiki 스킬(저장) + 옵시디언(열람)
- **토큰 절약 트릭**: Playwright로 NotebookLM 브라우저를 CLI에서 제어 → 직접 웹서치보다 토큰 아낌
- **Hermes Agent에 LLM Wiki 내장**: `/notebooklm-llm-wiki-flow` GitHub 레포를 설치하면 스킬로 사용 가능
- **Claude Code·OpenCode·Codex에서도 동작**: 에이전트 무관하게 동일 패턴 적용 가능
- **실전 시연**: 원달러 환율 × 코스피 30년 상관관계 조사 → 자동으로 entities, concepts, sources 생성
- **결과**: 단일 쿼리로 위키링크 형식의 복수 노트(소스, 엔티티, 컨셉, 비교 보고서) 자동 생성

## 관련 도구

- [[entities/tools/notebooklm]] — 조사 엔진 역할
- [[entities/tools/hermes-agent]] — LLM Wiki 스킬이 내장된 에이전트 CLI
- [[entities/tools/obsidian-web-clipper]] — 자료 수집 도구

## 연결

- [[concepts/llm-wiki]] — 이 워크플로우의 이론적 기반
- [[sources/옵시디언-주식분석-llm위키]] — 비슷한 맥락의 실전 적용 사례
