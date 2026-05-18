---
title: eGovFrame (전자정부 표준프레임워크)
type: entity
subtype: tool
tags: [egovframe, java, spring, 공공, 전자정부]
---

# eGovFrame (전자정부 표준프레임워크)

행정안전부가 주도하는 대한민국 공공 정보시스템 개발 표준 프레임워크. Spring Boot 기반. 공공기관 시스템 구축 시 사실상 표준.

## Spring AI / Langchain4j 공식 지원 (v5.0.0)

eGovFrame 5.0.0부터 `egovframe-boot-starter-parent`에 Spring AI와 Langchain4j 의존성 관리를 공식 포함. BOM 없이 parent 선언만으로 버전 명시 없이 사용 가능.

**Spring AI 관리 의존성 (v1.0.1):**
- `spring-ai-client-chat`, `spring-ai-rag`
- `spring-ai-starter-model-ollama`, `spring-ai-starter-vector-store-pgvector`, `spring-ai-starter-vector-store-redis`
- `spring-ai-pdf-document-reader`, `spring-ai-markdown-document-reader`

**Langchain4j 관리 의존성 (v1.8.0 / v1.8.0-beta15):**
- `langchain4j`, `langchain4j-ollama`, `langchain4j-redis`, `langchain4j-spring-boot-starter`

```xml
<parent>
    <groupId>org.egovframe.boot</groupId>
    <artifactId>egovframe-boot-starter-parent</artifactId>
    <version>5.0.0</version>
</parent>
<!-- 버전 명시 없이 바로 사용 가능 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-model-ollama</artifactId>
</dependency>
```

## 연결

- [[concepts/spring-ai]] — 공식 지원 AI 프레임워크
- [[concepts/langchain4j]] — 공식 지원 AI 프레임워크
