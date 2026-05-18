---
title: HuggingFace 모델을 활용한 RAG
type: concept
tags: [rag, huggingface, embedding, 벡터DB, langchain, spring-ai, 한국어rag]
sources: []
---

# HuggingFace 모델을 활용한 RAG

HuggingFace Hub의 임베딩 모델과 생성 모델을 조합해 RAG(Retrieval-Augmented Generation) 파이프라인을 구축하는 방법. OpenAI API 없이 완전 오픈소스 RAG를 구현할 수 있다.

---

## 1. RAG 파이프라인 전체 구조

```
[문서 인덱싱 단계]
문서 → 청크 분할 → 임베딩(bge-m3) → 벡터 DB 저장

[질의 응답 단계]
질문 → 임베딩 → 벡터 DB 검색 → Top-K 청크 → LLM(Llama/Mistral) → 답변
```

---

## 2. LangChain + HuggingFace (Python)

가장 보편적인 조합.

### 설치

```bash
pip install langchain langchain-huggingface langchain-community
pip install faiss-cpu chromadb  # 벡터 DB (둘 중 선택)
pip install sentence-transformers
```

### 기본 RAG 파이프라인

```python
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.llms import HuggingFacePipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from transformers import pipeline
import torch

# 1. 임베딩 모델 설정
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={"device": "cuda"},
    encode_kwargs={"normalize_embeddings": True}
)

# 2. 문서 로드 & 청킹
loader = PyPDFLoader("document.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " ", ""]
)
chunks = splitter.split_documents(docs)

# 3. 벡터 스토어 생성 (FAISS — 로컬, 빠름)
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index")  # 디스크 저장

# 로드 (재시작 시)
vectorstore = FAISS.load_local("faiss_index", embeddings)

# 4. LLM 설정 (HuggingFace 모델)
llm_pipe = pipeline(
    "text-generation",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    max_new_tokens=512,
    temperature=0.1,
    do_sample=True,
)
llm = HuggingFacePipeline(pipeline=llm_pipe)

# 5. RAG 체인 구성
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # 모든 청크를 프롬프트에 직접 삽입
    retriever=vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    ),
    return_source_documents=True
)

# 6. 질의
result = qa_chain.invoke({"query": "문서에서 RAG에 대해 설명해주세요"})
print(result["result"])
print("출처:", [doc.metadata for doc in result["source_documents"]])
```

### 한국어 최적화 프롬프트

```python
from langchain.prompts import PromptTemplate

korean_rag_template = """다음 컨텍스트를 기반으로 질문에 한국어로 답변해주세요.
컨텍스트에 없는 내용은 "제공된 문서에서 해당 정보를 찾을 수 없습니다"라고 답하세요.

컨텍스트:
{context}

질문: {question}

답변:"""

prompt = PromptTemplate(
    template=korean_rag_template,
    input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)
```

---

## 3. 벡터 DB 선택 가이드

### FAISS (Facebook AI Similarity Search)

```python
from langchain_community.vectorstores import FAISS

# 로컬 파일 기반, 서버 불필요
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("./faiss_index")

# 유사도 + MMR(다양성) 검색
retriever = vectorstore.as_retriever(
    search_type="mmr",  # Maximum Marginal Relevance
    search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.7}
)
```

**적합한 경우:** 소규모 프로젝트, 서버리스, 프로토타입

### Chroma

```python
from langchain_community.vectorstores import Chroma

# 영구 저장소
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db",
    collection_name="my_docs"
)

# 메타데이터 필터링
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 5,
        "filter": {"source": "document.pdf", "page": {"$gte": 10}}
    }
)
```

**적합한 경우:** 개발/테스트, 메타데이터 필터링 필요

### pgvector (PostgreSQL)

```python
from langchain_community.vectorstores import PGVector

CONNECTION_STRING = "postgresql+psycopg2://user:password@localhost:5432/mydb"

vectorstore = PGVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    connection_string=CONNECTION_STRING,
    collection_name="documents",
    pre_delete_collection=False  # 기존 데이터 유지
)
```

**적합한 경우:** 이미 PostgreSQL 사용 중, 기업 환경, ACID 필요

### Milvus / Weaviate (대규모)

```python
# Milvus — 수억 개 벡터 처리
from langchain_community.vectorstores import Milvus

vectorstore = Milvus.from_documents(
    documents=chunks,
    embedding=embeddings,
    connection_args={"host": "localhost", "port": "19530"},
    collection_name="rag_docs",
    index_params={"index_type": "IVF_FLAT", "metric_type": "IP", "nlist": 1024}
)
```

**벡터 DB 선택 매트릭스:**

| DB | 규모 | 설치 | 필터링 | 특이사항 |
|----|------|------|--------|----------|
| FAISS | ~100만 | 매우 쉬움 | 제한적 | 순수 로컬, 파일 기반 |
| Chroma | ~10만 | 쉬움 | 좋음 | 개발용 최적 |
| pgvector | ~500만 | 보통 | 매우 좋음 | PostgreSQL 확장 |
| Qdrant | ~1억 | 보통 | 매우 좋음 | Rust 기반, 빠름 |
| Milvus | ~10억+ | 어려움 | 좋음 | 대규모 전용 |
| Weaviate | ~1억 | 보통 | 매우 좋음 | GraphQL API |

---

## 4. Spring AI + HuggingFace 연동 (Java)

### 4-1. HuggingFace Inference API 연동

```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-transformers-spring-boot-starter</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-huggingface-spring-boot-starter</artifactId>
</dependency>
```

```yaml
# application.yml
spring:
  ai:
    huggingface:
      api-key: ${HF_TOKEN}
      chat:
        options:
          model: HuggingFaceH4/zephyr-7b-beta  # 채팅 모델
      embedding:
        options:
          model: BAAI/bge-m3  # 임베딩 모델
```

```java
@Service
public class RagService {

    private final EmbeddingModel embeddingModel;
    private final VectorStore vectorStore;
    private final ChatClient chatClient;

    // Spring AI Auto-configuration으로 주입됨
    public RagService(EmbeddingModel embeddingModel,
                      VectorStore vectorStore,
                      ChatModel chatModel) {
        this.embeddingModel = embeddingModel;
        this.vectorStore = vectorStore;
        this.chatClient = ChatClient.builder(chatModel).build();
    }

    public String query(String question) {
        return chatClient.prompt()
            .advisors(QuestionAnswerAdvisor.builder(vectorStore).build())
            .user(question)
            .call()
            .content();
    }
}
```

### 4-2. Transformers.java (로컬 ONNX 모델)

Spring AI는 `spring-ai-transformers-spring-boot-starter`를 통해 ONNX 모델을 JVM에서 직접 실행 가능.

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-transformers-spring-boot-starter</artifactId>
</dependency>
```

```yaml
spring:
  ai:
    transformers:
      embedding:
        options:
          # HuggingFace Hub에서 ONNX 모델 자동 다운로드
          model-name: "intfloat/multilingual-e5-large"
          # 또는 로컬 경로
          # model-path: "/opt/models/multilingual-e5-large"
        tokenizer:
          options:
            max-length: 512
            padding: true
            truncation: true
```

```java
@Configuration
public class EmbeddingConfig {

    @Bean
    public EmbeddingModel localEmbeddingModel(
            TransformersEmbeddingModel model) {
        // 배치 처리 설정
        return model;
    }
}

@Service
public class EmbeddingService {

    @Autowired
    private EmbeddingModel embeddingModel;

    public List<Double> embed(String text) {
        EmbeddingRequest request = new EmbeddingRequest(
            List.of(text),
            EmbeddingOptions.EMPTY
        );
        EmbeddingResponse response = embeddingModel.call(request);
        return response.getResult().getOutput();
    }

    // 문서 인덱싱
    public void indexDocuments(List<String> texts) {
        List<Document> docs = texts.stream()
            .map(t -> new Document(t))
            .toList();
        vectorStore.add(docs);  // 내부에서 embeddingModel 호출
    }
}
```

### 4-3. Ollama + HuggingFace 모델 로컬 RAG

```yaml
# Ollama로 HuggingFace 모델 로컬 실행
spring:
  ai:
    ollama:
      base-url: http://localhost:11434
      chat:
        options:
          model: llama3.1:8b  # HuggingFace Llama 3.1 기반
      embedding:
        options:
          model: nomic-embed-text  # HuggingFace nomic 기반
```

```bash
# Ollama에서 HuggingFace 모델 사용
ollama run llama3.1:8b         # Meta Llama 3.1
ollama run nomic-embed-text    # nomic-ai/nomic-embed-text-v1.5
ollama run bge-m3              # BAAI/bge-m3
```

---

## 5. 고급 RAG 패턴

### 5-1. Hybrid Search (Dense + Sparse)

```python
from langchain_community.vectorstores import Qdrant
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

# Dense retriever (벡터 검색)
dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Sparse retriever (BM25 키워드 검색)
bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 5

# Ensemble (가중 결합)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.4, 0.6]  # sparse 40% + dense 60%
)

results = ensemble_retriever.invoke("한국 경제 전망")
```

### 5-2. Multi-Query Retrieval

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

# LLM으로 질문을 여러 관점으로 재생성
multi_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)
# "한국 경제는?" → 
#   "한국의 GDP 성장률은?", 
#   "한국 경제의 주요 문제점은?",
#   "한국 주식시장 전망은?" 등으로 확장
```

### 5-3. Contextual Compression

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# 검색된 청크에서 관련 부분만 추출
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever()
)
```

### 5-4. Self-RAG (Self-Reflective RAG)

```python
# RAG 결과를 LLM이 스스로 평가해 재검색 결정
from langchain_core.output_parsers import JsonOutputParser

grade_prompt = """문서가 질문에 답하기에 관련성 있으면 "yes", 없으면 "no"를 JSON으로 반환.
문서: {document}
질문: {question}
JSON: {{"score": "yes" or "no"}}"""

def grade_documents(question, docs):
    relevant = []
    for doc in docs:
        result = llm.invoke(grade_prompt.format(
            document=doc.page_content, question=question
        ))
        if "yes" in result.lower():
            relevant.append(doc)
    return relevant
```

---

## 6. 완전 오픈소스 RAG 스택 추천

### 소규모 (개인/프로토타입)

```
임베딩: BAAI/bge-m3 (로컬, ONNX)
벡터 DB: FAISS (로컬 파일)
LLM: Ollama + Llama 3.1 8B (로컬)
프레임워크: LangChain or Spring AI
비용: $0
```

### 중규모 (팀/서비스)

```
임베딩: BAAI/bge-m3 (HuggingFace Inference Endpoints)
벡터 DB: pgvector (PostgreSQL)
LLM: HuggingFace Inference Endpoints (Llama 3.1 70B) 또는 Groq API
프레임워크: LangChain / Spring AI
비용: ~$200-500/월
```

### 대규모 (엔터프라이즈)

```
임베딩: 자체 호스팅 (Inference Endpoints A10G)
벡터 DB: Milvus 또는 Qdrant 클러스터
LLM: 자체 파인튜닝 모델 (QLoRA) + Inference Endpoints
프레임워크: LangChain / LlamaIndex + Kubernetes
비용: $3,000-10,000/월+
```

---

## 연결

- [[entities/tools/huggingface]] — HuggingFace 플랫폼 개요
- [[concepts/huggingface-embedding]] — 임베딩 모델 상세 (MTEB, ONNX)
- [[concepts/rag]] — RAG 개념 전반
- [[concepts/spring-ai]] — Spring AI RAG 구현 상세
- [[concepts/langchain4j]] — Java용 LangChain4j RAG 구현
- [[entities/tools/ollama]] — 로컬 LLM 실행
