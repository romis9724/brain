---
updated: 2026-06-08
source_count: 30
page_count: 76
---

# Overview

Romis의 세컨드 브레인 현황 요약.
새 자료가 추가될 때마다 LLM이 이 페이지를 업데이트합니다.

---

## 현재 지식 도메인

### LLM / AI 지식 관리
이 브레인의 설계 기반이 되는 패턴인 [[concepts/llm-wiki]]와 관련 생태계에 대한 지식.
[[entities/people/안드레이-카파시]]가 제안한 패턴과 실전 구현 사례 두 건이 수록됨.
추가로 eGovFrame 세미나 자료에서 Spring AI / Langchain4j 기반 RAG 실무 구현 방법 수록.
HuggingFace 플랫폼 종합 정리(플랫폼 개요·Hub·라이브러리·임베딩·RAG·Spring AI 연동·라이선스·비용) 신규 추가.
**Adaptive Chunking (LREC 2026)**: RAG 청킹 단계를 문서별 최적 전략으로 자동 선택하는 프레임워크 추가. 모델 변경 없이 RAG 성능 62%→72% 향상 사례.

→ 핵심 개념: [[concepts/llm-wiki]], [[concepts/rag]], [[concepts/pkm]], [[concepts/spring-ai]], [[concepts/langchain4j]], [[concepts/huggingface-embedding]], [[concepts/huggingface-rag]]
→ 관련 도구: [[entities/tools/notebooklm]], [[entities/tools/obsidian-web-clipper]], [[entities/tools/qmd]], [[entities/tools/hermes-agent]], [[entities/tools/ollama]], [[entities/tools/egovframe]], [[entities/tools/huggingface]]
→ 원본 자료: [[sources/llm-wiki-카파시]], [[sources/notebooklm-cli-llm위키-튜토리얼]], [[sources/옵시디언-주식분석-llm위키]], [[sources/spring-ai-langchain4j-rag-egovframe]], [[sources/adaptive-chunking-rag]]

### 투자 / 가상자산 — 데이트레이딩 (기존)
이더리움·알트코인 데이트레이딩 전략에 관한 지식.
15분봉 기반 기술적 분석 자동매매 규칙이 핵심.

→ 관련 개념: [[concepts/기술적-분석]], [[concepts/데이트레이딩]]
→ 원본 자료: [[sources/가상자산-데이트레이딩-전략]]

### 투자 / 가상자산 — 코인 매매전략 (신규 대규모 추가)
YouTube "코인 매매 전략" 검색으로 수집된 247개 영상에서 추출한 코인 단기 매매 지식.
비트코인·알트코인 단타·스캘핑, 보조지표 활용, 선물거래, 자동매매봇이 핵심 도메인이다.

→ 핵심 개념 (신규 4개):
  - [[concepts/스캘핑]] — 초단기 포지션 매매, 1~5분봉 기반
  - [[concepts/코인-자동매매봇]] — 파이썬·챗GPT·노코드 플랫폼 자동화 전략
  - [[concepts/코인-선물거래]] — 레버리지·롱숏·ICT 기법, 97% 손실 원인 분석
  - [[concepts/알트코인-투자전략]] — 섹터별 알트코인 접근법, 비트코인 도미넌스 연동
  - [[concepts/코인-보조지표-활용]] — MACD·볼린저밴드·RSI·스토캐스틱·일목균형표 실전 활용
  - [[concepts/코인-자동매매-데이트레이딩-추천전략]] — 3종 전략·리스크관리·구현 우선순위 종합 가이드 (query 결과 저장)
→ 원본 소스 (테마별 5개, 247개 영상 통합):
  - [[sources/코인매매-비트코인-전략]] — 비트코인 가격 전략, 파동 분석, 실시간 대응 (~90개 영상)
  - [[sources/코인매매-단타-스캘핑]] — 이동평균·스캘핑·시초가 단타 기법 (~35개 영상)
  - [[sources/코인매매-지표-활용]] — MACD·볼린저밴드·RSI·일목균형표 지표별 강의 (~16개 영상)
  - [[sources/코인매매-선물-레버리지]] — 선물 기초·ICT·VWAP·변동성 돌파 (~25개 영상)
  - [[sources/코인매매-자동매매봇]] — 파이썬 봇·챗GPT 자동화·마틴게일 실험 (~11개 영상)
  - [[sources/코인매매-알트코인-종목별]] — 이더리움·솔라나·도지·AI코인 개별 종목 분석 (~27개 영상)

### 투자 / 미국 ETF (신규)
[[entities/people/송팀장]] 유튜브 채널에서 수집한 나스닥100 구조 변화 분석. 2026년 5월 1일 발효된 룰 변경이 단순 편입 가속이 아닌 **패시브 ETF 구조 자체를 내부자 엑시트 유동성으로 재편하는 것**임을 명확히 한다.

→ 핵심 개념: [[concepts/ETF-패시브투자]], [[concepts/나스닥100-인덱스-룰변경]]
→ 핵심 인물: [[entities/people/송팀장]]
→ 원본 소스: [[sources/나스닥ETF-룰변경-송팀장]]

### 투자 / 경제 분석 — 김영익 채널
[[entities/people/김영익]] 서강대 교수의 유튜브 채널 398개 영상에서 추출한 거시경제·투자전략 지식.
경기순환 기반 자산배분, 코스피·채권·환율·섹터 분석이 핵심 도메인이다.

→ 핵심 개념: [[concepts/자산배분]], [[concepts/경기순환]], [[concepts/금리와-채권]], [[concepts/원달러-환율]], [[concepts/코스피-투자전략]]
→ 핵심 인물: [[entities/people/김영익]]
→ 원본 소스 (테마별 7개):
  - [[sources/김영익-자산배분-투자전략]] — 포트폴리오 4분법, 리밸런싱 전략
  - [[sources/김영익-코스피-경기전망]] — 선행지수 기반 코스피 방향성 분석 (~170개 영상)
  - [[sources/김영익-채권-금리-분석]] — 채권 특강, FOMC·한국은행 긴급진단
  - [[sources/김영익-환율-달러-분석]] — 달러 인덱스·원달러 환율 전략
  - [[sources/김영익-섹터-종목-분석]] — 반도체·ETF·개별종목 분석
  - [[sources/김영익-경제스쿨-특강]] — 한국경제 구조 분석, 노후투자, 자본주의 심층 강의
  - [[sources/김영익-2026년-전략]] — 2026년 글로벌 자산배분·ETF·돈의흐름

### AI 창업 / 경영 (신규 확장)
[[entities/people/민상기]]의 위노트 1인 SaaS 창업 사례에서 확장. **[[entities/people/노정석]] 비팩토리 대표**의 AI 네이티브 경영 실전 사례 추가. 업무의 70~80%를 AI 에이전트로 대체하는 운영 방식, 채용 기준 변화, 주니어 암묵지 소멸 문제 등.

→ 핵심 개념: [[concepts/ai-네이티브-경영]], [[concepts/1인-saas-창업]]
→ 핵심 인물: [[entities/people/노정석]], [[entities/people/민상기]]
→ 원본 자료: [[sources/ai-네이티브-기업-노정석-비팩토리]]

### AI 인프라 & 투자 (신규)
[[entities/people/김지현]] SK 부사장의 토큰 이코노미 프레임. AI 데이터센터의 4단계 병목(반도체→전력→네트워크→데이터) 구조와 메모리 기업의 꽃놀이패 포지션 분석.

→ 핵심 개념: [[concepts/ai-인프라-토큰-이코노미]]
→ 핵심 인물: [[entities/people/김지현]]
→ 원본 자료: [[sources/ai-데이터센터-병목-김지현]]

### AI 도구 — 영상 생성 (신규)
xAI Grok Imagine Video 1.5 레퍼런스 가이드. Aurora MoE 엔진, 6가지 생성 모드, 프롬프트 작성법.

→ 원본 자료: [[sources/grok-imagine-video-1-5]]

---

## 통계

| 항목 | 수량 |
|------|------|
| 원본 자료 | 30 (sources 페이지 기준) |
| wiki 페이지 | 76 |
| 도메인 | 9 (LLM/AI 지식관리, 투자/가상자산, 투자/경제분석, 투자/미국ETF, AI창업, AI네이티브경영, AI인프라투자, 부동산/도시, 창업/화장품) |
| 인물 | 9 (Andrej Karpathy, 김영익, 김광석, 송팀장, 민상기, 하조은, 김시덕, 노정석, 김지현) |
| 도구 | 7 (NotebookLM, Web Clipper, qmd, Hermes Agent, Ollama, eGovFrame, HuggingFace) |
| 처리된 원본 영상/문서 | 651개 (김영익 398개 + 코인매매전략 247개 + 단건 6개) |
