---
title: LLM Wiki (Andrej Karpathy 원본)
type: source
date: 2026-05-15
source_file: raw/external/llm-wiki.md
origin: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
tags: [llm-wiki, 지식관리, pkm, 세컨드브레인]
---

# LLM Wiki — Andrej Karpathy 원본 문서

## 한 줄 요약

LLM이 RAG처럼 매번 재발견하는 대신, 지속적으로 유지되는 wiki를 직접 작성·관리하게 하여 지식이 복리로 축적되는 패턴.

## 핵심 포인트

- **RAG와의 차이**: RAG는 질문마다 원본에서 재발견. LLM Wiki는 지식을 한 번 컴파일하고 최신 상태로 유지
- **3계층 구조**: Raw sources(불변) → Wiki(LLM 작성) → Schema(CLAUDE.md, 운영 지침)
- **3가지 오퍼레이션**: Ingest(새 자료 처리), Query(wiki 기반 답변), Lint(건강 검진)
- **index.md + log.md**: 카탈로그와 이력을 별도 파일로 관리해 LLM 내비게이션 효율화
- **좋은 답변은 wiki에 저장**: 탐색과 질의가 지식 베이스를 더 풍요롭게 만듦
- **선택적 CLI 도구**: qmd 같은 로컬 검색 엔진으로 확장 가능
- **Vannevar Bush의 Memex(1945)와 연결**: 연상 경로가 있는 개인 큐레이션 지식 저장소

## 이 브레인과의 관계

이 저장소(`romis9724/brain`)는 이 문서의 패턴을 직접 구현한 것.
CLAUDE.md가 schema 역할, wiki/ 가 LLM-generated layer 역할.

## 연결

- [[concepts/llm-wiki]] — 이 문서에서 추출한 핵심 개념 페이지
- [[concepts/rag]] — LLM Wiki가 극복하려는 기존 방식
- [[entities/people/안드레이-카파시]] — 원저자
- [[entities/tools/qmd]] — 문서에서 언급된 검색 도구
- [[entities/tools/obsidian-web-clipper]] — 자료 수집 도구로 언급
