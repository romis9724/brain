---
title: Langchain4j
type: concept
tags: [langchain4j, java, llm, rag, 생성형ai]
sources: [[sources/spring-ai-langchain4j-rag-egovframe]]
---

# Langchain4j

Java 용 LLM 통합 프레임워크. Python의 LangChain을 Java 생태계에 맞게 재설계하는 것을 목적으로 2023년 출시. 2025년 기준 버전 1.0.0 정식 출시.

## 핵심 특징

Spring AI와의 가장 큰 차이: **AiServices Reflection 기반 프록시 패턴**.  
Spring Data JPA에서 Repository 인터페이스만 정의하면 구현체가 자동 생성되는 것과 동일한 패턴.

```java
// Spring Data JPA 패턴과 동일한 구조
interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByName(String name); // 메서드 시그니처만 정의
}

// Langchain4j AI Services
interface RagChatbot {
    @SystemMessage("당신은 도움이 되는 AI입니다")
    String chat(@UserMessage String query); // 메서드 시그니처만 정의
}
// Langchain4j가 런타임에 프록시 구현체를 자동 생성
```

## AiServices 사용 흐름

```java
// 1단계: 인터페이스 정의
interface RagChatbot {
    @SystemMessage("당신은 도움이 되는 AI입니다")
    String chat(@UserMessage String query);
}

// 2단계: 프록시 생성
RagChatbot bot = AiServices.builder(RagChatbot.class)
    .chatModel(model)
    .contentRetriever(retriever)  // RAG 자동 적용
    .chatMemory(memory)           // Chat Memory 자동 관리
    .build();

// 3단계: 사용
String response = bot.chat(userQuery);
```

## Spring AI와의 비교

| 구분 | Spring AI | Langchain4j |
|------|-----------|-------------|
| 핵심 패턴 | Advisor Chain | AiServices Reflection 기반 프록시 |
| 구현 방식 | ChatClient + Advisor Chain | 인터페이스 + 어노테이션 |
| 사용자 메시지 | `.user("…")` 메서드 | `@UserMessage` 어노테이션 |
| RAG 적용 | `RetrievalAugmentationAdvisor` | `contentRetriever()` 빌더 |
| Chat Memory | `MessageChatMemoryAdvisor` | `chatMemory()` 빌더 |

- **Spring AI**: 명시적 Advisor 체인 조합. 각 단계가 순차적으로 처리. 커스텀 세밀
- **Langchain4j**: 인터페이스 선언만으로 구현. 코드가 간결. Spring과 독립적으로 사용 가능

## 선택 기준

- **Spring AI 선택**: 기존 Spring Boot 프로젝트, 세밀한 RAG 커스텀 필요, Micrometer 관측성 필요
- **Langchain4j 선택**: 선언적·간결한 코드 선호, Spring 의존 없이 사용, Quarkus 등 다른 Java 프레임워크와 통합

## eGovFrame 지원

eGovFrame 5.0.0부터 `egovframe-boot-starter-parent`에 Langchain4j 공식 포함.
- 정식 릴리즈: `langchain4j`, `langchain4j-ollama`, `langchain4j-redis`, `langchain4j-spring-boot-starter` (v1.8.0)
- Beta: pgvector, embeddings, reactor, easy-rag, pdf-parser (v1.8.0-beta15)

## 연결

- [[concepts/spring-ai]] — 비교 대상 프레임워크
- [[concepts/rag]] — RAG 구현 방식
- [[entities/tools/egovframe]] — 공식 지원 프레임워크
