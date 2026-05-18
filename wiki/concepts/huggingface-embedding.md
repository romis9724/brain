---
title: HuggingFace 임베딩 (Embedding)
type: concept
tags: [embedding, sentence-transformers, mteb, onnx, 한국어임베딩, 벡터]
sources: []
---

# HuggingFace 임베딩 (Embedding)

텍스트를 고차원 벡터로 변환하는 기술. RAG, 의미 검색, 클러스터링, 분류 등 다양한 NLP 태스크의 기반. HuggingFace는 sentence-transformers 라이브러리와 Hub를 통해 임베딩 모델의 사실상 표준 플랫폼이 됐다.

---

## 1. sentence-transformers 라이브러리

SBERT(Sentence-BERT) 논문(2019, Reimers & Gurevych) 기반의 문장 임베딩 전용 라이브러리.

### 기본 사용법

```python
from sentence_transformers import SentenceTransformer
import numpy as np

# 모델 로드
model = SentenceTransformer("BAAI/bge-m3")

# 단일/복수 문장 임베딩
sentences = [
    "HuggingFace는 AI 플랫폼입니다.",
    "Hugging Face is an AI platform.",
    "인공지능 오픈소스 플랫폼 허깅페이스"
]
embeddings = model.encode(sentences)
print(embeddings.shape)  # (3, 1024)

# 코사인 유사도 계산
from sentence_transformers import util
cos_sim = util.cos_sim(embeddings[0], embeddings[1])
print(f"유사도: {cos_sim.item():.4f}")  # 0.85~0.95 수준
```

### Bi-Encoder vs Cross-Encoder

```python
# Bi-Encoder: 빠름, RAG 검색에 적합
bi_encoder = SentenceTransformer("BAAI/bge-m3")
query_emb = bi_encoder.encode("RAG란 무엇인가?")
doc_embs = bi_encoder.encode(documents)  # 미리 인덱싱 가능

# Cross-Encoder: 정확함, 리랭킹에 적합
from sentence_transformers import CrossEncoder
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# 쿼리-문서 쌍 점수
scores = cross_encoder.predict([
    ("RAG란 무엇인가?", doc1),
    ("RAG란 무엇인가?", doc2),
])
```

**RAG 2단계 검색 패턴 (Bi → Cross):**
```
쿼리 → [Bi-Encoder 검색] → Top-100 후보 → [Cross-Encoder 리랭킹] → Top-5 최종
```

### 배치 처리 & GPU 최적화

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3", device="cuda")

# 대용량 배치 처리
large_corpus = [...]  # 수십만 문장

embeddings = model.encode(
    large_corpus,
    batch_size=256,
    show_progress_bar=True,
    normalize_embeddings=True,  # 코사인 유사도용 L2 정규화
    convert_to_numpy=True
)

# 디스크에 저장
import numpy as np
np.save("corpus_embeddings.npy", embeddings)
```

---

## 2. MTEB 벤치마크

**MTEB (Massive Text Embedding Benchmark)** — HuggingFace에서 운영하는 임베딩 모델 표준 벤치마크.

### 벤치마크 구성

| 태스크 유형 | 설명 | 예시 데이터셋 |
|-------------|------|---------------|
| Retrieval | 쿼리-문서 검색 | BEIR (MSMARCO, NQ, HotpotQA) |
| STS | 의미적 유사도 | STS-B, SICK-R |
| Classification | 텍스트 분류 | Banking77, SST2 |
| Clustering | 클러스터링 | ArXiv, Reddit |
| Reranking | 재랭킹 | AskUbuntu, MindSmall |
| PairClassification | 쌍 분류 | SprintDuplicateQuestions |
| Summarization | 요약 품질 | SummEval |

### MTEB 리더보드 상위 모델 (2024년 기준)

| 순위 | 모델 | 파라미터 | 차원 | 평균 점수 |
|------|------|----------|------|----------|
| 1 | voyage-3-large | — | 1024 | 72.8 |
| 2 | text-embedding-3-large (OpenAI) | — | 3072 | 72.0 |
| 3 | **BAAI/bge-en-icl** | 7B | 4096 | 71.7 |
| 4 | **Salesforce/SFR-Embedding-2_R** | 7B | 4096 | 71.4 |
| 5 | **BAAI/bge-m3** (다국어) | 570M | 1024 | 69.3 |
| 10 | **intfloat/multilingual-e5-large** | 560M | 1024 | 64.8 |

> 오픈소스 중 BAAI/bge-m3가 다국어 최강, 영어 특화는 bge-en-icl 또는 SFR-Embedding-2_R.

### 한국어 특화 벤치마크

MTEB Korean Subset 포함 (KLUE-STS, Ko-StrategyQA 등):

| 모델 | 한국어 STS | 한국어 Retrieval | 비고 |
|------|-----------|----------------|------|
| BAAI/bge-m3 | 87.2 | 73.4 | 다국어 범용 최강 |
| dragonkue/snowflake-arctic-embed-l-v2.0-ko | 88.5 | 75.1 | 한국어 특화 파인튜닝 |
| intfloat/multilingual-e5-large | 84.1 | 68.9 | 무난한 다국어 |
| snunlp/KR-ELECTRA-discriminator | 82.3 | 65.2 | 한국어 인코더, 임베딩 용도 |
| BM-K/KoSimCSE-roberta | 83.7 | — | 한국어 SimCSE |

---

## 3. 주요 임베딩 모델 상세

### BAAI/bge-m3 (추천 — 다국어 범용)

| 속성 | 값 |
|------|-----|
| 파라미터 | 570M |
| 임베딩 차원 | 1024 |
| 최대 토큰 | 8192 |
| 지원 언어 | 100개+ |
| 라이선스 | MIT |
| 특이사항 | Dense + Sparse + Multi-vector 동시 지원 |

```python
from FlagEmbedding import BGEM3FlagModel

# bge-m3의 3가지 검색 방식 동시 사용
model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)

embeddings = model.encode(
    ["What is RAG?", "RAG란 무엇인가?"],
    batch_size=12,
    max_length=8192,
    return_dense=True,
    return_sparse=True,
    return_colbert_vecs=True
)

# Dense: 코사인 유사도
# Sparse: BM25 유사 어휘 매칭
# ColBERT: 토큰 레벨 세밀한 매칭
```

**Hybrid 검색 (Dense + Sparse 결합):**
```python
def hybrid_score(dense_score, sparse_score, alpha=0.5):
    return alpha * dense_score + (1 - alpha) * sparse_score
```

### intfloat/multilingual-e5 계열

```python
# multilingual-e5-large (권장)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/multilingual-e5-large")

# 중요: passage/query 접두사 필요
query = "query: 한국의 수도는?"
passage = "passage: 서울은 대한민국의 수도입니다."

q_emb = model.encode(query, normalize_embeddings=True)
p_emb = model.encode(passage, normalize_embeddings=True)

similarity = (q_emb * p_emb).sum()
```

| 모델 | 차원 | 파라미터 | 특징 |
|------|------|----------|------|
| multilingual-e5-small | 384 | 117M | 경량, 빠름 |
| multilingual-e5-base | 768 | 278M | 균형 |
| multilingual-e5-large | 1024 | 560M | 정확도 최강 |

### OpenAI 호환 무료 대안

```python
# nomic-embed-text — 맥락 길이 8192, Apache 2.0
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)

# 접두사 필수
query_emb = model.encode("search_query: 한국어 문장")
doc_emb = model.encode("search_document: 문서 내용")
```

---

## 4. ONNX 변환 방법

ONNX 변환 시 추론 속도 2~4배 향상, CPU 환경에서 특히 효과적.

### optimum 라이브러리 활용 (권장)

```python
from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import AutoTokenizer
import numpy as np

# 방법 1: 자동 변환 (내부에서 export=True)
model = ORTModelForFeatureExtraction.from_pretrained(
    "BAAI/bge-m3",
    export=True,  # 자동으로 ONNX 변환 수행
    provider="CPUExecutionProvider"  # or "CUDAExecutionProvider"
)
tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")

# 추론
inputs = tokenizer("임베딩할 문장", return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)
embeddings = outputs.last_hidden_state[:, 0, :]  # CLS 토큰
```

### 직접 변환 (세밀한 제어)

```python
from optimum.exporters.onnx import main_export

# ONNX 내보내기
main_export(
    model_name_or_path="intfloat/multilingual-e5-large",
    output="./onnx_models/multilingual-e5-large",
    task="feature-extraction",
    opset=17,  # ONNX opset 버전
    optimize="O3",  # 최적화 수준 (O1~O4)
)
```

### ONNX Runtime 직접 사용

```python
import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

# 세션 생성 (CPU 최적화 옵션)
sess_options = ort.SessionOptions()
sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
sess_options.intra_op_num_threads = 4

session = ort.InferenceSession(
    "./onnx_models/model.onnx",
    sess_options=sess_options,
    providers=["CPUExecutionProvider"]
)

tokenizer = AutoTokenizer.from_pretrained("intfloat/multilingual-e5-large")

def embed(texts: list[str]) -> np.ndarray:
    encoded = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="np"
    )
    outputs = session.run(
        None,
        {
            "input_ids": encoded["input_ids"],
            "attention_mask": encoded["attention_mask"],
            "token_type_ids": encoded.get("token_type_ids",
                np.zeros_like(encoded["input_ids"]))
        }
    )
    # CLS 토큰 추출 후 L2 정규화
    embeddings = outputs[0][:, 0, :]
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    return embeddings / norms

# 속도 비교
# PyTorch CPU: ~150ms/배치
# ONNX CPU: ~40ms/배치
```

### 양자화 (Quantization) — 추가 속도 향상

```python
from optimum.onnxruntime import ORTQuantizer
from optimum.onnxruntime.configuration import AutoQuantizationConfig

# INT8 동적 양자화
quantizer = ORTQuantizer.from_pretrained("./onnx_models/multilingual-e5-large")
qconfig = AutoQuantizationConfig.avx512_vnni(
    is_static=False,  # 동적 양자화
    per_channel=False
)
quantizer.quantize(
    quantization_config=qconfig,
    save_dir="./onnx_quantized"
)
# 결과: 모델 크기 ~4배 감소, 속도 ~2배 향상, 정확도 ~1-2% 감소
```

---

## 5. 실전 임베딩 선택 가이드

```
한국어 포함 다국어 프로젝트
  └─ BAAI/bge-m3                 ← 1순위 (정확도 최강, MIT)
  └─ intfloat/multilingual-e5-large ← 2순위 (빠른 추론)

영어 전용 고성능
  └─ BAAI/bge-en-icl             ← LLM 기반, 최고 정확도
  └─ Salesforce/SFR-Embedding-2_R ← 범용 고성능

경량/엣지 환경
  └─ intfloat/multilingual-e5-small ← 384차원, 빠름
  └─ BAAI/bge-small-en-v1.5         ← 영어 경량

OpenAI API 대체
  └─ nomic-ai/nomic-embed-text-v1.5 ← 8192 토큰 맥락, Apache 2.0
  └─ thenlper/gte-large              ← 무난한 성능
```

---

## 연결

- [[entities/tools/huggingface]] — HuggingFace 플랫폼 전체 개요
- [[concepts/huggingface-rag]] — 임베딩 모델을 RAG에 적용하는 방법
- [[concepts/rag]] — RAG 개념 전반
- [[concepts/spring-ai]] — Spring AI에서 HuggingFace 임베딩 모델 사용
