---
title: Ollama
type: entity
subtype: tool
tags: [ollama, llm, 로컬ai, 오픈소스]
---

# Ollama

로컬 환경에서 오픈소스 LLM을 쉽게 다운로드, 실행, 관리할 수 있는 도구. vLLM, llama.cpp 계열과 달리 설치 및 사용이 간단해 로컬 PC에서 빠른 테스트와 개발에 적합.

## 기본 사용법

```bash
ollama pull <model-name>                                    # 모델 다운로드
ollama pull hf.co/<username>/<model-repository>           # HuggingFace에서 다운로드
ollama run <model-name>                                     # 모델 실행
ollama list                                                 # 설치된 모델 목록
```

## Spring AI / Langchain4j 연동

Spring AI의 `spring-ai-starter-model-ollama`, Langchain4j의 `langchain4j-ollama` 의존성으로 로컬 LLM을 Spring 코드에 통합 가능. API 키 없이 로컬에서 완전히 동작.

## 특징

- 로컬 실행으로 데이터 프라이버시 보장
- 다양한 오픈소스 모델 지원 (Llama, Qwen, Mistral 등)
- REST API 제공으로 다양한 클라이언트와 통합 용이
- HuggingFace 모델 직접 pull 가능

## 연결

- [[concepts/spring-ai]] — Spring AI에서 Ollama 모델 사용
- [[concepts/langchain4j]] — Langchain4j에서 Ollama 연동
