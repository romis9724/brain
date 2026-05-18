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

## [2026-05-16] query | 코인 자동매매 데이트레이딩 추천 매매기법 정리

- 참조 페이지: `sources/가상자산-데이트레이딩-전략`, `sources/코인매매-자동매매봇`, `sources/코인매매-단타-스캘핑`, `concepts/코인-자동매매봇`, `concepts/코인-보조지표-활용`, `concepts/데이트레이딩`
- 목적: 자동매매 프로그램 개발용 agent 전달 정보 정리
- 출처: 247개 영상 ingest 기반 wiki 통합 정보
- 저장 페이지: `wiki/concepts/코인-자동매매-데이트레이딩-추천전략.md` (신규 생성)

## [2026-05-18] ingest | 김영익 35개 영상 전사 재ingest + 송팀장 나스닥 ETF 룰 변경 전사 ingest

- 대상: `raw/external/김영익/` 35개 전사 업데이트 파일 + `raw/external/송팀장/` 1개 신규 파일
- 처리 방식: 20개 초과 → 도메인별 배치 (6개 테마)
- 업데이트된 wiki 소스 페이지 (7개):
  - `김영익-코스피-경기전망.md` — 명목GDP 적정주가 3,200~3,400, M2 대비 시총 62%, 버핏지수 한국-미국 비교
  - `김영익-채권-금리-분석.md` — 시장금리 선행성, 금리인상 사이클 종료, 채권 전환 임박
  - `김영익-환율-달러-분석.md` — 달러 3차 하락(2~3년 30%), 원화 19% 저평가, 순대외채 18조
  - `김영익-섹터-종목-분석.md` — 반도체 정점 타이밍, HBM vs 범용 이원화, 금 30% 과대평가
  - `김영익-자산배분-투자전략.md` — 은행예금 45% 재배분, 부동산→금융자산 전환, 미국주식 68% 과다
  - `김영익-경제스쿨-특강.md` — 스태그플레이션 조짐, M2 급락, 고용 질적 악화, 신용등급 위험
  - `나스닥ETF-룰변경-송팀장.md` — 4가지 룰 상세(패스트엔트리/팬텀시총/플로트×3/분기리밸런싱), 손익구조표, 2026년 메가IPO 4조달러

## [2026-05-18] lint | wiki 건강 검진

- 전체 검사 파일: 53개
- 깨진 링크: 0개 ✓
- 고아 페이지: 0개 ✓
- 통계 불일치 수정:
  - `index.md` total_pages 59→53, total_sources 19→20
  - `index.md` ## Sources (16)→(20), ## Concepts (15)→(22), ### 기술적 분석 (7)→(8)
  - `overview.md` source_count 19→20, page_count 59→53, 통계 테이블 동기화
- 결론: 링크 무결성 이상 없음. 누적 오버카운트 수정 완료

## [2026-05-18] ingest | Spring AI 및 Langchain4j를 활용한 생성형 AI 및 RAG 지원 (eGovFrame 세미나)

- 원본: `raw/informations/(6부) Spring AI 및 Langchain4j를 활용한 생성형 AI 및 RAG 지원.pdf`
- eGovFrame(전자정부 표준프레임워크) 세미나 자료 53페이지 PDF
- 신규 생성 (5개):
  - `wiki/sources/spring-ai-langchain4j-rag-egovframe.md` — 소스 요약 (핵심 포인트, 코드 패턴)
  - `wiki/concepts/spring-ai.md` — Spring AI 개념·Advisors API·Portable API 상세
  - `wiki/concepts/langchain4j.md` — Langchain4j·AiServices 프록시 패턴·Spring AI 비교
  - `wiki/entities/tools/ollama.md` — 로컬 LLM 실행 도구
  - `wiki/entities/tools/egovframe.md` — 전자정부 표준프레임워크·공식 지원 의존성 목록
- 업데이트 (1개): `wiki/concepts/rag.md` — RAG 3단계 프로세스, Spring AI 구현 패턴 보강
- 총 wiki 페이지: 50 → 56 (+6), 총 소스: 18 → 19 (+1)
- 주요 인사이트: Spring AI(Advisor Chain) vs Langchain4j(AiServices 프록시) 패턴 비교 수록

## [2026-05-18] query | HuggingFace 종합 정리

- 요청 항목: 플랫폼 개요, Hub 기능, 라이브러리 생태계, 임베딩 특화, RAG 활용, 서비스/인프라, 오픈소스 LLM, Spring AI/Java 연동, 라이선스, 비용 구조
- 신규 생성:
  - `wiki/entities/tools/huggingface.md` — 플랫폼 전체 개요 (역사·펀딩·Hub 3종·라이브러리 10종·오픈소스 LLM·인프라·라이선스·비용)
  - `wiki/concepts/huggingface-embedding.md` — sentence-transformers 상세, MTEB 벤치마크, 주요 임베딩 모델, ONNX 변환 방법
  - `wiki/concepts/huggingface-rag.md` — HuggingFace 모델 RAG 구현 (LangChain·Spring AI·Java 연동, 벡터 DB 선택 가이드, 고급 RAG 패턴)
- 업데이트: `wiki/overview.md`, `index.md`
- 총 wiki 페이지: 56 → 59 (+3), 도구: 6 → 7 (+1)
- Spring AI [[concepts/spring-ai]], RAG [[concepts/rag]], Ollama [[entities/tools/ollama]] 기존 페이지와 양방향 크로스 레퍼런스 완료

## [2026-05-17] ingest | 나스닥 ETF 룰 변경 — 송팀장

- 원본: `raw/external/송팀장/나스닥 ETF 룰이 바뀌었습니다 — 지금 적립 중이라면 꼭 보세요.md`
- 채널: 송팀장 (2026.05.13 업로드), 자막 포함 (yt-dlp VTT 추출)
- 신규 생성:
  - `wiki/sources/나스닥ETF-룰변경-송팀장.md`
  - `wiki/concepts/나스닥100-인덱스-룰변경.md` (패스트엔트리·팬텀시총·플로트3배·분기리밸런싱 4가지 상세)
  - `wiki/concepts/ETF-패시브투자.md` (패시브 ETF 구조·취약점·대안)
  - `wiki/entities/people/송팀장.md`
- 업데이트: `wiki/overview.md`, `index.md` (도메인 신규 추가: 투자/미국ETF)
- 도메인 확장: 투자/미국ETF 신규 섹터 신설
- 총 wiki 페이지: 45 → 50 (+5), 총 소스: 17 → 18 (+1), 처리 영상 누계: 646 → 647개

## [2026-05-16] ingest | 국민성장펀드 vs 반도체 ETF 단건 영상

- 원본: `raw/external/youtube/국민성장펀드 vs 반도체 ETF  같은 3000만원, 5년 뒤 손에 쥐는 돈이 다릅니다.md`
- 자막 없음 (IP 차단으로 자막 수집 실패) — 제목 기반 ingest
- 신규 생성: `wiki/sources/국민성장펀드-vs-반도체ETF.md`
- 연결 개념: `자산배분`, `코스피-투자전략`
- 총 wiki 페이지: 43 → 44, 총 소스: 16 → 17
