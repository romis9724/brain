---
title: Spring AI
type: concept
tags: [spring-ai, java, llm, rag, 생성형ai]
sources: [[sources/spring-ai-langchain4j-rag-egovframe]]
---

# Spring AI

Java/Spring 생태계에서 생성형 AI 기능을 통합하는 공식 Spring 프레임워크. Python 중심이던 AI 프레임워크(LangChain, LlamaIndex)를 Java 개발자가 Spring 친화적인 방식으로 사용할 수 있게 한다.

## 핵심 설계 철학

기존 데이터와 API를 AI 모델과 연결하는 문제에 집중. 엔터프라이즈 환경에서 AI 기능을 자연스럽게 구현하도록 설계.

```yaml
# application.yml 설정 변경만으로 AI 제공자 교체
spring.ai.openai.api-key: ${OPENAI_KEY}
# → spring.ai.anthropic.api-key: ${ANTHROPIC_KEY} 로만 바꾸면 전환
```

## Portable API (이식 가능한 API)

동일 코드로 여러 AI 제공자 사용 가능:
- **Chat**: OpenAI, Anthropic(Claude), Ollama, Google(Gemini) 등
- **Embedding**: OpenAI, Ollama, Azure 등
- **Image**: OpenAI(DALL-E), Stability AI
- **Audio**: OpenAI(Whisper, TTS)
- **Multimodal**: OpenAI(GPT-4V), Anthropic(Claude)

```java
// 제공자와 무관한 동일 코드
@Autowired
private ChatModel chatModel;

public String chat(String message) {
    return chatModel.call(message);
}
```

## Spring Native Integration

- `@Configuration`, `@Bean`을 통한 선언적 설정
- `application.yml` 기반 외부화된 설정
- Auto-configuration 및 Spring Boot Starter 제공

## Advanced Features

- **Function Calling**: LLM에게 Java 메서드 호출 위임
- **Structured Output**: JSON 형식 응답
- **Streaming**: 실시간 스트리밍 응답
- **RAG**: Advisors API를 통한 검색 증강 생성
- **Prompt Caching**: Claude Sonnet/Opus/Haiku 등 일부 모델 지원
- **Observability**: Micrometer 통합(메트릭, 트레이싱)

## Advisors API — RAG 핵심 추상화

RAG 흐름 전체를 추상화. AOP의 Advice처럼 ChatClient 파이프라인에 삽입:

| Advisor | 용도 |
|---------|------|
| `QuestionAnswerAdvisor` | 단순 RAG. 빠른 시작, 커스텀 제한 |
| `RetrievalAugmentationAdvisor` | 모듈형 RAG. 각 단계 커스텀 가능 |
| `MessageChatMemoryAdvisor` | 대화 이력 관리 |
| `VectorStoreChatMemoryAdvisor` | VectorStore 기반 채팅 메모리 |

**Modular RAG 단계 커스텀:**
- Pre-Retrieval: `RewriteQueryTransformer`, `CompressionQueryTransformer`, `TranslationQueryTransformer`, `MultiQueryExpander`
- Retrieval: `VectorStoreDocumentRetriever`
- Post-Retrieval: `DocumentJoiner`, `ContextualQueryAugmenter`

## Vector Store 지원

Redis, Chroma, Pinecone, Weaviate, PostgreSQL(PGvector) 등. 메타데이터 필터링 지원.

## eGovFrame 지원

eGovFrame 5.0.0부터 `egovframe-boot-starter-parent`에 Spring AI 1.0.1 공식 포함. BOM 없이 의존성 바로 사용 가능.

## 연결

- [[concepts/rag]] — RAG 개념 및 3단계 프로세스
- [[concepts/langchain4j]] — 비교 대상 프레임워크
- [[entities/tools/ollama]] — 로컬 LLM 실행
- [[entities/tools/egovframe]] — 공식 지원 프레임워크
