---
title: 옵시디언으로 나만의 주식 분석 AI 만들기 | 카파시 'LLM Wiki' 실전 적용
type: source
date: 2026-05-15
source_file: raw/external/옵시디언으로 나만의 주식 분석 AI 만들기  카파시 'LLM Wiki' 실전 적용.md
origin: https://www.youtube.com/watch?v=4JaN0NNvY_o
author: 기획자 데이먼
published: 2026-04-27
tags: [llm-wiki, 옵시디언, 주식분석, pkm, claude-code]
related: [[concepts/llm-wiki]], [[concepts/pkm]], [[entities/people/안드레이-카파시]]
---

# 옵시디언으로 주식 분석 LLM Wiki 실전 적용

## 한 줄 요약

Claude Code + 옵시디언으로 국내 주식 분석 LLM Wiki를 구축한 사례. 웹 클리퍼로 뉴스를 raw/에 수집하면 LLM이 자동으로 종목·섹터·테마·매크로 페이지를 생성·갱신.

## 핵심 포인트

- **구조**: raw/(뉴스 스크랩) → CLAUDE.md(스키마) → wiki/(LLM 생성)
- **수집**: Obsidian Web Clipper로 뉴스·유튜브 스크립트를 raw/에 원클릭 저장
- **ingest 명령**: 터미널에서 "ingest 해줘" → LLM이 종목 페이지 신규 생성 + 기존 섹터/테마/매크로 업데이트
- **query**: "삼성전자 지금 투자해도 될까?" → wiki 기반 답변 (빠르고 저렴)
- **lint**: 잘못 연결된 크로스 레퍼런스, 오래된 정보, 고아 페이지 자동 정리. 스케줄링 권장
- **옵시디언 장점**: 위키링크 탐색, 로컬 그래프 뷰(문서 관계 시각화), 테마/섹터/매크로 그루핑

## PKM 관점 비교

| 방식 | 관리 주체 | 특징 |
|------|-----------|------|
| PARA 프레임워크 | 사람 | 직접 분류·관리·업데이트 |
| ACE 프레임워크 | 사람 | 에이스 구조로 PKM |
| **LLM Wiki** | **LLM** | raw 데이터만 던지면 AI가 모든 정리 |

> "개인 일기·경험 기록은 내가 직접 관리. 조사·연구 영역은 LLM에게 위임." — 기획자 데이먼

## 연결

- [[concepts/llm-wiki]] — 이 사례의 이론적 기반
- [[concepts/pkm]] — PARA·ACE·LLM Wiki 비교 맥락
- [[sources/notebooklm-cli-llm위키-튜토리얼]] — 유사한 실전 구현 사례
- [[entities/tools/obsidian-web-clipper]] — 핵심 수집 도구
