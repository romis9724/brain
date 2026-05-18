# Brain — 운영 스키마

이 저장소는 Romis의 개인 세컨드 브레인입니다.
LLM(Claude Code)이 wiki를 작성·유지하고, 사람(Romis)은 자료를 공급하고 질문합니다.

---

## 디렉토리 구조

```
brain/
├── CLAUDE.md          ← 이 파일. LLM 운영 지침
├── index.md           ← 전체 wiki 페이지 카탈로그
├── log.md             ← 작업 이력 (append-only)
├── raw/               ← 원본 자료 (읽기 전용, 절대 수정 금지)
│   ├── assets/        ← 이미지 등 첨부파일
│   ├── memories/      ← AI 메모리에서 내보낸 나에 대한 정보
│   ├── external/      ← 외부에서 가져온 참고자료
│   └── informations/  ← 별개로 제공된 정보들
└── wiki/              ← LLM이 작성·관리하는 지식 페이지
    ├── overview.md     ← 전체 지식 베이스 현황 요약
    ├── concepts/       ← 개념·이론·방법론 페이지
    ├── entities/       ← 인물·도구·회사·프로젝트
    │   ├── people/
    │   ├── tools/
    │   └── projects/
    └── sources/        ← 원본 자료 요약 페이지
```

---

## 페이지 frontmatter 형식

모든 wiki 페이지는 YAML frontmatter로 시작합니다.

### sources/ 페이지
```yaml
---
title: 페이지 제목
type: source
date: YYYY-MM-DD
source_file: raw/파일명.md
tags: [태그1, 태그2]
---
```

### concepts/ 페이지
```yaml
---
title: 개념 이름
type: concept
tags: [태그1, 태그2]
sources: [[출처페이지1]]
---
```

### entities/ 페이지
```yaml
---
title: 엔티티 이름
type: entity
subtype: person | tool | project | company | book
tags: [태그1]
---
```

---

## 워크플로

### Ingest (새 자료 추가)

자료를 `raw/` 에 넣고 "ingest 해줘" 또는 파일명을 언급하면 아래 순서로 처리합니다.

1. **자료 읽기** — `raw/파일명` 전체 읽기
2. **핵심 논의** — 주요 인사이트, 의문점, 연결점을 사용자와 짧게 논의
3. **sources/ 페이지 생성** — `wiki/sources/파일명-슬러그.md` 작성
   - 한 문단 요약
   - 핵심 포인트 (bullet)
   - 기존 개념·엔티티와의 연결
4. **concepts/ 업데이트** — 새로 등장하거나 보강된 개념 페이지 생성·수정
5. **entities/ 업데이트** — 등장한 인물·도구·프로젝트 페이지 생성·수정
6. **overview.md 업데이트** — 전체 요약에 새 지식 반영
7. **index.md 업데이트** — 새로 생성된 페이지 추가
8. **log.md 기록** — `## [YYYY-MM-DD] ingest | 자료 제목` 형식으로 추가

하나의 자료가 10-15개의 wiki 페이지에 영향을 줄 수 있습니다.

### Query (질문 응답)

1. **index.md 먼저 읽기** — 관련 페이지 파악
2. **관련 wiki 페이지 읽기** — concepts/, entities/, sources/ 중 해당 페이지
3. **답변 작성** — 출처 페이지 링크 포함
4. **가치 있는 답변은 wiki에 저장** — 분석·비교·새로운 연결을 발견했다면 `wiki/concepts/` 또는 별도 페이지로 저장하고 index.md에 추가
5. **log.md 기록** — `## [YYYY-MM-DD] query | 질문 요약` 형식으로 추가

### Lint (건강 검진)

"lint 해줘" 명령 시 아래 항목을 점검합니다.

- 페이지 간 모순·상충 내용
- 더 최신 자료에 의해 superseded된 오래된 주장
- 인바운드 링크가 없는 고아 페이지
- 언급은 됐지만 페이지가 없는 개념·엔티티
- 빠진 크로스 레퍼런스
- 보완하면 좋을 자료 제안

---

## index.md 유지 규칙

- 모든 wiki 페이지는 index.md에 등록
- 형식: `- [[페이지경로|페이지제목]] — 한 줄 요약`
- 카테고리: Overview, Sources, Concepts, Entities (People / Tools / Projects)
- ingest·query 결과로 페이지가 추가될 때마다 즉시 업데이트

## log.md 유지 규칙

- Append-only: 절대 기존 항목 수정·삭제 금지
- 형식: `## [YYYY-MM-DD] <타입> | <제목>`
  - 타입: `ingest`, `query`, `lint`, `update`
- 세션 시작 시 마지막 5개 항목을 읽어 최근 맥락 파악

---

## 크로스 레퍼런스 컨벤션

- Obsidian 위키링크 사용: `[[파일명]]` 또는 `[[파일명|표시텍스트]]`
- 페이지 내 관련 개념은 첫 등장 시 링크
- 파일명은 한국어 가능, kebab-case 영문 혼용 가능
- 태그는 소문자 영문 또는 한국어 (예: `#투자`, `#기술적분석`)

---

## 중요 원칙

- `raw/` 파일은 절대 수정하지 않음
- wiki 페이지는 LLM이 작성, 사람은 읽기 위주
- 좋은 답변은 wiki에 저장해 지식이 축적되게 함
- 매 세션 시작 시 `log.md` 마지막 항목들을 읽어 맥락 파악
