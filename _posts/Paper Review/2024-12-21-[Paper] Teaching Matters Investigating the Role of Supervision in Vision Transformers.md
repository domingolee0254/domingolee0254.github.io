---  
title: "[Paper] Teaching Matters: Investigating the Role of Supervision in Vision Transformers"  
author_profile: false  
toc: true  
toc_label: "Table of Contents"  
toc_icon: true  
toc_sticky: true  
categories:  
    - Paper Review
tags:  
    - Vision Transformers
    - Self-supervised Learning
    - Attention Mechanisms
    - Computer Vision
last_modified_at: 2024-12-21  
---

# **Summary**

- Problem:  
  - Vision Transformers(ViTs)의 학습 방식이 주목 패턴, 표현 학습, 다운스트림 작업 성능에 미치는 영향을 충분히 이해하지 못함.  
  - 대부분의 기존 연구가 명시적 감독(explicit supervision)에 초점.  

- Goal:  
  - ViT의 다양한 학습 방식(supervised, contrastive self-supervised, reconstructive self-supervised)을 비교하여 각 방식이 ViT의 행동에 어떻게 영향을 미치는지 분석.  

- Observation:  
  - ViT는 CNN과 달리 지역(local) 및 전역(global) 정보를 학습하는 방식에 유연성이 있음.  
  - 학습 방식에 따라 정보 처리 순서와 표현 방식이 달라짐.  

- Key Idea:
  - How ViTs process local/global information (Attention).
  - What we take away from ViTs (Features).
  - Why we use ViTs (Downstream Tasks).
  - Offset Local Attention Head와 같은 새로운 현상을 발견하고 이를 ViT의 필수 메커니즘으로 정의.  
  - ViT는 다양한 학습 방식에 따라 다운스트림 작업에서 적합한 레이어가 다르게 나타날 수 있음.  

- Result:
  - 결국, 모든 다운스트림 작업에 최적화된 모델이나 레이어는 없으며, 작업에 따라 적합한 레이어가 달라짐.
  - supervised은 이미지 수준에서 가장 풍부한 의미적 표현을 제공.  
  - contrastive learning은 경쟁력을 보이며, reconstructive learning도 의미 있는 표현을 학습함.  
  - 특정 다운스트림 작업에 최적화된 레이어는 작업별로 달라질 수 있음.  

---

# **Strong**  

1. 6가지 학습 방식(supervised 2개, contrastive 2개, reconstructive 2개)을 비교하여 ViT의 학습 특성을 심층적으로 탐구.  

2. Offset Local Attention Head라는 새로운 현상을 발견하고 이를 ViT의 구조적 필수 요소로 정의.  

3. 다운스트림 작업에 적합한 최적의 레이어를 제시, 실제 응용 가능성을 높임.  

---

# **Weakness**  

1. 작업 의존성: 모든 다운스트림 작업에 적합한 단일 모델이나 레이어는 존재하지 않음.  

2. 다른 요인 미탐구: attention에 초점이 맞춰져 있으며, 다른 구조적 변형 요소는 다루지 않음.  

---

# **Comment**  

1. ViT가 다양한 학습 방식에서 보이는 유연성과 잠재력을 강조하며, 이는 향후 모델 설계에 중요한 통찰을 제공.  

2. 다운스트림 작업에 적합한 레이어와 학습 방법을 제안해, 실제 응용에서 유용한 방향성을 제시.  

3. Offset Local Attention Head의 역할과 성능 영향을 추가로 분석하면 의미 있는 후속 연구가 가능.  

---

# **Questions**  

1. 이 연구 결과가 다른 작업(NLP 등)이나 변형된 ViT 구조에도 적용될 수 있을까?  

2. CNN의 인덕티브 바이어스를 도입하면 ViT의 성능과 학습 효율에 어떤 영향을 미칠까?  

3. 명시적 학습과 자가 지도 학습의 강점을 결합하면 더 일관적이고 우수한 결과를 낼 수 있을까?  

4. 대규모 데이터 처리 시 모델의 연산량과 레이턴시는 실질적으로 문제가 되지 않을까?  

5. 다양한 비전 데이터셋에 대한 검증으로 결과의 일반성을 입증할 필요가 있지 않을까?  

---
