# Log

작업 이력. Append-only — 기존 항목 수정·삭제 금지.
형식: `## [YYYY-MM-DD] <타입> | <제목>`

---

## [2026-05-15] ingest | 가상자산 데이트레이딩 자동매매 전략 요약

- 원본: `raw/informations/crypto_trading_strategy_summary.md`
- 생성 페이지: `wiki/sources/가상자산-데이트레이딩-전략.md`
- 업데이트 페이지: `wiki/concepts/기술적-분석.md`, `wiki/concepts/데이트레이딩.md`, `wiki/overview.md`
- 세컨드 브레인 시스템 초기 구축 및 첫 자료 ingest

## [2026-05-15] ingest | LLM Wiki 관련 자료 3건

- 원본 3개: `raw/external/llm-wiki.md`, `raw/external/NotebookLM을 CLI로...md`, `raw/external/옵시디언으로 나만의...md`
- 신규 생성 (11개):
  - sources: `llm-wiki-카파시.md`, `notebooklm-cli-llm위키-튜토리얼.md`, `옵시디언-주식분석-llm위키.md`
  - concepts: `llm-wiki.md`, `pkm.md`, `rag.md`
  - entities/people: `안드레이-카파시.md`
  - entities/tools: `notebooklm.md`, `obsidian-web-clipper.md`, `qmd.md`, `hermes-agent.md`
- 업데이트: `wiki/overview.md`, `index.md`
- 도메인 확장: LLM/AI 지식관리 영역 개설

## [2026-05-16] lint | wiki 건강 검진

- 전체 검사 파일: 15개
- 깨진 링크: 0개 ✓
- 고아 페이지: 0개 ✓
- Index 누락: 0개 ✓
- 통계 정확성: OK ✓
- 결론: wiki 상태 정상. 모든 링크 무결성 확인됨

## [2026-05-16] ingest | 김영익 채널 398개 영상 배치 처리

- 원본: `raw/external/김영익/` (398개 영상 클립, 대부분 자막 없음, 27개 전사 포함)
- 처리 방식: 20개 초과 → 도메인 그룹화 방식 (6개 테마 소스 페이지 + entity + concept 5개)
- 신규 생성 (17개):
  - entities/people: `김영익.md`
  - concepts: `자산배분.md`, `경기순환.md`, `금리와-채권.md`, `원달러-환율.md`, `코스피-투자전략.md`
  - sources: `김영익-자산배분-투자전략.md`, `김영익-코스피-경기전망.md`, `김영익-채권-금리-분석.md`, `김영익-환율-달러-분석.md`, `김영익-섹터-종목-분석.md`, `김영익-경제스쿨-특강.md`, `김영익-2026년-전략.md`
- 업데이트: `wiki/overview.md` (통계·도메인 갱신), `index.md` (총 32페이지·11소스)
- 도메인 확장: 투자/경제분석 — 김영익 섹터 신설
- 총 wiki 페이지: 15 → 32 (+17), 총 소스: 4 → 11 (+7)

## [2026-05-16] ingest | 코인매매전략 247개 영상 배치 처리

- 원본: `raw/external/코인매매전략/` (247개 영상 클립, YouTube "코인 매매 전략" 검색 수집)
- 처리 방식: 20개 초과 → 도메인 그룹화 방식 (6개 테마 소스 페이지 + concept 5개 신규 생성)
- 신규 생성 (11개):
  - concepts: `스캘핑.md`, `코인-자동매매봇.md`, `코인-선물거래.md`, `알트코인-투자전략.md`, `코인-보조지표-활용.md`
  - sources: `코인매매-비트코인-전략.md` (~90개), `코인매매-단타-스캘핑.md` (~35개), `코인매매-지표-활용.md` (~16개), `코인매매-선물-레버리지.md` (~25개), `코인매매-자동매매봇.md` (~11개), `코인매매-알트코인-종목별.md` (~27개)
- 업데이트: `wiki/overview.md` (통계·도메인 갱신), `index.md` (총 43페이지·16소스)
- 도메인 확장: 투자/가상자산 — 코인 매매전략 섹터 신설
- 기존 개념 보강: `기술적-분석.md`, `데이트레이딩.md` 관련 소스 추가
- 총 wiki 페이지: 32 → 43 (+11), 총 소스: 11 → 16 (+5), 처리 영상 누계: 645개
