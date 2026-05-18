---
title: HuggingFace (허깅페이스)
type: entity
subtype: tool
tags: [huggingface, llm, embedding, rag, nlp, 오픈소스, 머신러닝]
---

# HuggingFace (허깅페이스)

ML 모델·데이터셋·데모를 공유하는 플랫폼이자, `transformers` 등 핵심 오픈소스 라이브러리를 운영하는 AI 기업. "AI의 GitHub"로 불린다.

---

## 1. 회사 개요 & 역사

| 항목 | 내용 |
|------|------|
| 설립 | 2016년, 뉴욕 |
| 공동창업자 | Clément Delangue, Julien Chaumond, Thomas Wolf |
| 초기 제품 | 챗봇 앱 (10대 대상) |
| 피벗 | 2018년 BERT 공개 이후 NLP 플랫폼으로 전환 |
| 본사 | 뉴욕 (R&D 거점은 파리) |
| 직원 | ~500명 (2024년 기준) |

### 펀딩 이력

| 라운드 | 시기 | 금액 | 주요 투자자 |
|--------|------|------|-------------|
| Series A | 2019 | $15M | — |
| Series B | 2021 | $40M | Addition, Lux Capital |
| Series C | 2022 | $100M | Coatue, A16Z |
| Series D | 2023 | $235M | Google, Amazon, Nvidia, Salesforce 등 | 
| **누적** | — | **~$395M** | 기업가치 $4.5B (2023 Series D 기준) |

> Amazon, Google, Nvidia, Salesforce, Intel이 모두 Series D에 참여. 빅테크 전체가 투자한 중립적 플랫폼 포지셔닝.

### 비즈니스 모델

```
무료 (개인/오픈소스)
  ├─ Hub 무제한 공개 모델·데이터셋
  ├─ Spaces (CPU 기본 무료)
  └─ Inference API (월 제한)

유료 (Pro / Enterprise)
  ├─ PRO: $9/월 — Inference API 확장, 비공개 모델
  ├─ Enterprise Hub: $20/사용자/월 — SSO, 감사 로그, 프라이빗 Spaces
  ├─ Inference Endpoints: 전용 GPU 인프라 (사용량 기반 과금)
  └─ AutoTrain: 노코드 파인튜닝 ($?)
```

---

## 2. Hub 기능

### 2-1. Model Hub

현재 **100만 개 이상의 모델** 호스팅 (2024년 기준).

```
모델 카드 (Model Card)
  ├─ 사용 방법 (예시 코드)
  ├─ 학습 데이터 & 방법론
  ├─ 성능 벤치마크
  ├─ 라이선스 정보
  └─ 한계점 & 편향성 경고

파일 구조
  ├─ config.json         ← 모델 구조
  ├─ tokenizer.json      ← 토크나이저
  ├─ model.safetensors   ← 가중치 (safetensors 형식 권장)
  └─ README.md           ← 모델 카드
```

**주요 기능:**
- **Gated Models**: 사용자 동의(e-mail 인증) 필요 모델 (Llama, Gemma 등)
- **Model Collections**: 관련 모델 묶음 (예: Llama 3 전체 계열)
- **Leaderboards**: LMSYS Chatbot Arena, Open LLM Leaderboard 등 연동
- **Trending**: 24h/7d/30d 다운로드 기준 트렌딩 모델
- **Spaces 연동**: 모델 페이지에서 바로 데모 실행

```python
from huggingface_hub import hf_hub_download, snapshot_download

# 단일 파일 다운로드
hf_hub_download(
    repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
    filename="config.json",
    token="hf_..."  # Gated 모델은 토큰 필요
)

# 전체 모델 다운로드
snapshot_download(
    repo_id="BAAI/bge-m3",
    local_dir="./models/bge-m3"
)
```

### 2-2. Dataset Hub

**60만 개 이상의 데이터셋** 호스팅.

```python
from datasets import load_dataset

# 클라우드에서 스트리밍 (메모리 효율)
ds = load_dataset(
    "squad",
    split="train",
    streaming=True  # 대용량 데이터셋에 필수
)

# 로컬 파일로 데이터셋 생성
ds = load_dataset("csv", data_files="my_data.csv")

# 한국어 데이터셋 예시
kowiki = load_dataset("wikipedia", "20220301.ko")
klue = load_dataset("klue", "sts")  # KLUE STS 벤치마크
```

**특징:**
- Apache Arrow 포맷 → 빠른 로딩, 메모리 매핑
- Parquet 네이티브 지원
- `datasets` 라이브러리와 완전 통합
- 데이터셋 카드 (Dataset Card): 수집 방법, 라이선스, 통계 포함

### 2-3. Spaces

**Gradio 또는 Streamlit** 기반 ML 앱 호스팅. 무료 CPU 인스턴스 제공.

```python
# Gradio 기반 Spaces 예시 (app.py)
import gradio as gr
from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")

def generate(prompt):
    return pipe(prompt, max_new_tokens=100)[0]["generated_text"]

demo = gr.Interface(fn=generate, inputs="text", outputs="text")
demo.launch()
```

**Spaces 하드웨어 옵션:**

| 등급 | CPU/GPU | 비용 |
|------|---------|------|
| Free | 2 vCPU, 16GB RAM | 무료 |
| T4 Small | T4 GPU | $0.60/hr |
| T4 Medium | T4 GPU, 2x RAM | $0.90/hr |
| A10G Small | A10G GPU | $1.05/hr |
| A10G Large | A10G × 4 | $3.15/hr |
| A100 Large | A100 × 8 | $23.52/hr |

---

## 3. 주요 라이브러리 생태계

### 3-1. transformers

가장 핵심 라이브러리. BERT 이후 모든 주요 트랜스포머 모델 지원.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Pipeline API (가장 쉬운 방법)
pipe = pipeline(
    "text-generation",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
output = pipe("한국의 수도는?", max_new_tokens=50)

# 저수준 API
tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    load_in_4bit=True  # bitsandbytes 양자화
)
```

**지원 태스크:**
- `text-generation`, `text2text-generation`
- `fill-mask`, `token-classification`, `text-classification`
- `question-answering`, `summarization`, `translation`
- `image-classification`, `object-detection`, `image-segmentation`
- `automatic-speech-recognition`, `text-to-speech`

### 3-2. datasets

데이터셋 로딩·처리·공유 라이브러리.

```python
from datasets import Dataset, DatasetDict, load_dataset

# 빠른 map 변환
def tokenize(example):
    return tokenizer(example["text"], truncation=True, max_length=512)

tokenized = dataset.map(tokenize, batched=True, num_proc=4)

# 필터링
filtered = dataset.filter(lambda x: len(x["text"]) > 100)

# 커스텀 데이터셋 허브에 업로드
dataset = Dataset.from_dict({"text": texts, "label": labels})
dataset.push_to_hub("my-org/my-dataset", private=True)
```

### 3-3. tokenizers

Rust 기반 고성능 토크나이저. transformers의 `fast` 토크나이저 백엔드.

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# 커스텀 BPE 토크나이저 학습
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
tokenizer.train(files=["wiki.txt"], trainer=trainer)
```

**특징:** Python 토크나이저 대비 수십 배 빠름, 병렬 처리 내장.

### 3-4. accelerate

분산 학습·멀티 GPU·TPU 코드 단순화 라이브러리.

```python
from accelerate import Accelerator

accelerator = Accelerator()
model, optimizer, train_dataloader = accelerator.prepare(
    model, optimizer, train_dataloader
)

for batch in train_dataloader:
    outputs = model(**batch)
    loss = outputs.loss
    accelerator.backward(loss)
    optimizer.step()
    optimizer.zero_grad()
```

**주요 기능:**
- 코드 변경 최소화로 단일 GPU → 멀티 GPU/TPU/CPU 전환
- `DeepSpeed`, `FSDP` 통합
- `device_map="auto"` 자동 모델 분산 지원

### 3-5. PEFT (Parameter-Efficient Fine-Tuning)

전체 모델 파인튜닝 없이 소수 파라미터만 업데이트하는 기법 모음.

```python
from peft import LoraConfig, get_peft_model, TaskType

# LoRA 설정
lora_config = LoraConfig(
    r=16,                           # LoRA rank
    lora_alpha=32,                  # 스케일링 계수
    target_modules=["q_proj", "v_proj"],  # 적용 레이어
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# trainable params: 3,407,872 || all params: 6,742,609,920 || trainable%: 0.0506
```

**지원 방법:**
- **LoRA**: Low-Rank Adaptation — 가장 널리 사용
- **QLoRA**: 4bit 양자화 + LoRA — 소비자 GPU(24GB)로 70B 파인튜닝 가능
- **Prefix Tuning**, **P-Tuning**, **Prompt Tuning**
- **IA³**, **AdaLoRA**

### 3-6. TRL (Transformer Reinforcement Learning)

RLHF, DPO, PPO 등 alignment 파인튜닝 라이브러리.

```python
from trl import SFTTrainer, DPOTrainer
from transformers import TrainingArguments

# SFT (Supervised Fine-Tuning)
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    args=TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        fp16=True,
    ),
    peft_config=lora_config,  # PEFT 통합
)
trainer.train()

# DPO (Direct Preference Optimization) — RLHF 대안
dpo_trainer = DPOTrainer(
    model=model,
    ref_model=ref_model,
    args=training_args,
    beta=0.1,
    train_dataset=dpo_dataset,  # {"prompt", "chosen", "rejected"} 형식
)
```

### 3-7. diffusers

이미지 생성 모델(Stable Diffusion, FLUX 등) 전용 라이브러리.

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

image = pipe(
    "a photo of an astronaut riding a horse",
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]
image.save("output.png")
```

### 3-8. optimum

다양한 하드웨어(ONNX Runtime, OpenVINO, TensorRT, Habana Gaudi 등)에 최적화된 추론 라이브러리.

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

# ONNX Runtime으로 최적화된 추론
model = ORTModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    export=True  # 자동으로 ONNX 변환
)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
```

### 3-9. sentence-transformers

문장 임베딩 특화 라이브러리. SBERT 논문 기반. → [[concepts/huggingface-embedding]] 참조

### 3-10. evaluate

모델 평가 메트릭 라이브러리.

```python
import evaluate

# 다양한 메트릭
bleu = evaluate.load("bleu")
rouge = evaluate.load("rouge")
bertscore = evaluate.load("bertscore")
accuracy = evaluate.load("accuracy")

# 사용 예시
results = bleu.compute(
    predictions=["번역된 문장입니다"],
    references=[["참조 번역 문장입니다"]]
)
# {'bleu': 0.43, 'precisions': [0.8, 0.5, ...], ...}
```

---

## 4. 주요 오픈소스 LLM 모델들

Hub에서 접근 가능한 주요 LLM:

| 모델 | 제공자 | 크기 | 라이선스 | 특이사항 |
|------|--------|------|----------|----------|
| Llama 3.1/3.3 | Meta | 8B~405B | Llama 3 Community | Gated, 상업적 사용 가능 (월 7억 사용자 미만) |
| Mistral 7B | Mistral AI | 7B | Apache 2.0 | 무제한 상업 사용 가능 |
| Mixtral 8x7B | Mistral AI | 47B(MoE) | Apache 2.0 | MoE 구조, 효율적 |
| Qwen 2.5 | Alibaba | 0.5B~72B | Qwen License | 다국어, 한국어 준수 |
| Gemma 2 | Google | 2B~27B | Gemma Terms | Gated, 연구/상업 가능 |
| Phi-3/4 | Microsoft | 3.8B~14B | MIT | 경량, 추론 강화 |
| DeepSeek-V3 | DeepSeek | 671B(MoE) | MIT | 비용 효율적 학습 |
| Command R+ | Cohere | 104B | CC-BY-NC-4.0 | RAG 특화 |
| EXAONE 3.5 | LG AI Research | 2.4B~7.8B | EXAONE License | 한국어 최강 |
| SOLAR | Upstage | 10.7B | Apache 2.0 | 한국어 강화 |
| HyperCLOVA X | NAVER | — | 비공개 | Hub에 일부만 공개 |

---

## 5. 서비스 / 인프라

### Inference API (서버리스)

무료 티어에서도 사용 가능한 REST API. 모든 public 모델에 바로 호출 가능.

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/BAAI/bge-m3"
headers = {"Authorization": "Bearer hf_..."}

def query(texts):
    return requests.post(
        API_URL,
        headers=headers,
        json={"inputs": texts, "options": {"wait_for_model": True}}
    ).json()

embeddings = query(["한국어 문장 예시", "Another sentence"])
```

**제한:**
- 무료: 분당 요청 수 제한 (모델별 상이)
- 모델 콜드 스타트 ~20초 (warm-up 시간)
- 대용량 모델 일부 제한

### Inference Endpoints (전용)

전용 GPU 인스턴스에 모델 배포. 프로덕션용.

```python
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="https://my-endpoint.us-east-1.aws.endpoints.huggingface.cloud",
    token="hf_..."
)

# 텍스트 생성
response = client.text_generation(
    "Explain RAG in Korean",
    max_new_tokens=200,
    temperature=0.7
)

# 임베딩
embeddings = client.feature_extraction("임베딩할 문장")
```

**가격 예시 (AWS us-east-1):**

| 인스턴스 | GPU | 비용 |
|----------|-----|------|
| Intel Xeon | CPU만 | $0.06/hr |
| T4 Medium | T4 × 1 | $0.60/hr |
| A10G Large | A10G × 4 | $6.00/hr |
| A100 Large | A100 × 8 | $23.52/hr |

### AutoTrain

노코드/로코드 파인튜닝 서비스.

```bash
# CLI로 파인튜닝
pip install autotrain-advanced

autotrain llm \
    --train \
    --model meta-llama/Llama-3.2-3B-Instruct \
    --data-path ./data \
    --text-column text \
    --lr 2e-4 \
    --epochs 3 \
    --batch-size 4 \
    --use-peft \
    --use-int4 \
    --push-to-hub \
    --username my-org \
    --repo-name my-finetuned-model
```

---

## 6. 라이선스 이슈

### 라이선스 종류별 상업적 사용 여부

| 라이선스 | 상업적 사용 | 수정/배포 | 주의사항 |
|----------|-------------|-----------|----------|
| **Apache 2.0** | 가능 | 가능 | 고지 의무 |
| **MIT** | 가능 | 가능 | 고지 의무 |
| **CC-BY 4.0** | 가능 | 가능 | 출처 표시 |
| **CC-BY-SA 4.0** | 가능 | 가능 | 동일 라이선스 |
| **CC-BY-NC 4.0** | **불가** | 가능 | 비상업 전용 |
| **Llama 3 Community** | 조건부 가능 | 가능 | 월 7억 MAU 미만, Llama 용도 표기 |
| **Gemma Terms** | 조건부 가능 | 가능 | 허용 사용 정책 동의 |
| **Qwen License** | 버전별 상이 | 가능 | Qwen 1.5까지는 상업 가능 |
| **OpenRAIL-M** | 조건부 가능 | 가능 | 사용 제한 조항 확인 필수 |
| **BigScience BLOOM** | 조건부 가능 | 가능 | 금지 사용 목록 존재 |

### 체크리스트 — 상업적 사용 전

1. 모델 카드 내 `License` 필드 확인
2. Gated 모델은 사용 약관 원문 검토
3. 학습 데이터 라이선스도 확인 (데이터 오염 문제)
4. 파인튜닝된 모델은 베이스 모델 + 파인튜닝 데이터 라이선스 모두 적용
5. 한국 기업: GDPR/개인정보보호법 관련 학습 데이터 출처 검토

---

## 7. 비용 구조

### 무료 티어

| 기능 | 제한 |
|------|------|
| 공개 모델 호스팅 | 무제한 |
| 비공개 모델 호스팅 | 1개 무료 (PRO: 무제한) |
| Inference API | 분당 제한 (모델별, 약 30~300 req/min) |
| Spaces (CPU) | 3개 무료 (슬립 후 콜드 스타트) |
| Datasets | 무제한 |

### 유료 플랜

| 플랜 | 가격 | 주요 혜택 |
|------|------|-----------|
| PRO | $9/월 | Inference API 확대, 비공개 모델 무제한, ZeroGPU 우선순위 |
| Enterprise Hub | $20/사용자/월 | SSO, 감사 로그, 프라이빗 Spaces, SLA |

### Inference Endpoints 비용 예시 (월 단위)

```
bge-m3 임베딩 서버 (CPU 전용, 소규모):
  Intel Xeon Large: $0.06/hr × 730hr ≈ $44/월

Llama 3.1 8B (A10G Small, 프로덕션):
  A10G Small: $1.05/hr × 730hr ≈ $767/월

비용 절감 전략:
  - 오토스케일: 0→N 자동 스케일 (유휴 시간 과금 최소화)
  - 스팟 인스턴스: ~70% 할인 (인터럽트 위험)
  - 서버리스 Inference API: 소규모 트래픽에 충분
```

---

## 연결

- [[concepts/huggingface-embedding]] — sentence-transformers 상세, MTEB, ONNX 변환
- [[concepts/huggingface-rag]] — HuggingFace 모델을 활용한 RAG 구현 상세
- [[concepts/spring-ai]] — Spring AI에서의 HuggingFace 모델 연동
- [[concepts/rag]] — RAG 개념 전반
- [[entities/tools/ollama]] — 로컬 LLM 실행 (HuggingFace 모델 기반)
