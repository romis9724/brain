---
title: Spring AI 및 Langchain4j를 활용한 생성형 AI 및 RAG 지원
type: source
date: 2026-05-18
source_file: raw/informations/(6부) Spring AI 및 Langchain4j를 활용한 생성형 AI 및 RAG 지원.pdf
tags: [spring-ai, langchain4j, rag, llm, 생성형ai, egovframe, java]
---

# Spring AI 및 Langchain4j를 활용한 생성형 AI 및 RAG 지원

eGovFrame(전자정부 표준프레임워크) 세미나 자료 (6부). Spring AI와 Langchain4j를 활용해 Java/Spring 환경에서 생성형 AI와 RAG를 구현하는 방법을 다루는 53페이지 발표 자료.

## 핵심 포인트

- **Spring AI**: Spring 생태계 내에서 다양한 AI 제공자(OpenAI, Anthropic, Ollama 등)를 통합 인터페이스로 추상화하는 프레임워크. `application.yml` 설정 변경만으로 AI 제공자 교체 가능
- **RAG 3단계 흐름**: (1) 문서 준비(ETL — Reader → Transformer → Writer → VectorStore), (2) 검색(사용자 쿼리 임베딩 → 유사도 검색), (3) 생성(Query + Context → LLM → Answer)
- **Advisors API**: Spring AI에서 RAG를 선언적으로 구성하는 핵심 추상화. `QuestionAnswerAdvisor`(간단), `RetrievalAugmentationAdvisor`(모듈형·커스텀 가능)
- **Modular RAG**: Pre-Retrieval(QueryTransformer, MultiQueryExpander) → Retrieval(DocumentRetriever) → Post-Retrieval(DocumentJoiner, QueryAugmenter) 단계별 커스텀
- **Langchain4j vs Spring AI**: Spring AI는 Advisor Chain 패턴(명시적 조합), Langchain4j는 AiServices Reflection 기반 프록시(인터페이스+어노테이션)
- **eGovFrame 5.0.0 공식 지원**: Spring AI 1.0.1, Langchain4j 1.8.0을 `egovframe-boot-starter-parent`에 포함 — BOM 없이 버전 명시 불필요
- **로컬 LLM**: Ollama로 오픈소스 LLM(Llama, Qwen 등) 로컬 실행, Onnx 변환 Embedding 모델로 외부 API 의존 제거
- **벡터 DB**: Redis Stack(RSALv2/SSPLv1 듀얼 라이선스 — 상용 시 라이선스 확인 필요), PgVector, Chroma, Pinecone 등 지원
- **실사례**: Spring AI ChatClient + Advisor 패턴으로 표준프레임워크 문서 기반 RAG Chatbot 구현. 유사도 임계값 0.70, topK=3 설정으로 score 0.88 수준 문서 3건 검색

## 주요 코드 패턴

**Spring AI — Advisor Chain**
```java
ChatClient chatClient = ChatClient.builder(chatModel)
    .advisors(
        new MessageChatMemoryAdvisor(chatMemory),
        new RetrievalAugmentationAdvisor(documentRetriever)
    ).build();
```

**Langchain4j — AiServices 프록시**
```java
interface RagChatbot {
    @SystemMessage("당신은 도움이 되는 AI입니다")
    String chat(@UserMessage String query);
}
RagChatbot bot = AiServices.builder(RagChatbot.class)
    .chatModel(model).contentRetriever(retriever).build();
```

## 연결

- [[concepts/spring-ai]] — Spring AI 개념 상세
- [[concepts/langchain4j]] — Langchain4j 개념 상세
- [[concepts/rag]] — RAG 개념 및 Spring AI 구현 (보강됨)
- [[entities/tools/ollama]] — 로컬 LLM 실행 도구
- [[entities/tools/egovframe]] — 전자정부 표준프레임워크
