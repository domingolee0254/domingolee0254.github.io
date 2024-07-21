---
title: "[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding"
author_profile: false
toc: True
toc_label: "Table of Contents"
toc_icon: True
toc_sticky:	True
categories: 
    - Paper Review
tags: 
    - Document Understanding
    - OCR
    - Vision Transformers
last_modified_at: 2022-07-21
---

# **Summary**
- 문제점:
  - 기존 모델들은 대부분 특정 언어로 된 문서만 처리할 수 있음.
  - 프리트레인 데이터가 부족한 언어의 문서를 학습하기 어려움.
  - 여러 언어를 처리하는 경우 문제가 발생함.
- Key idea:
  - 텍스트와 레이아웃 부분을 구분하여 처리할 수 있는 트랜스포머 구조 제안.
  - 문서의 형태가 동일하면 언어가 달라도 의미 파악이 용이함.
- 결과:
  - 다양한 언어에 대한 실험 결과 기존 SOTA 모델에 비해 F1 스코어 0.02 상승.

# **Strong**
1. LiLT 모델은 비교적 적은 데이터로도 높은 성능을 보이며, 영어로 Pre-Train되었음에도 불구하고 다국어 문서에서도 높은 성능을 보여줌.
2. 비동기 최적화 전략을 사용하여 텍스트와 레이아웃 흐름을 효과적으로 분리하고 결합함.
3. BiACM 메커니즘을 통해 언어 독립적인 교차 모달리티 상호작용을 강화함.

# **Weakness**
1. 일반화를 하기에 실험이 부족한 것 같음.
2. 모든 언어에 대해 동일한 수준의 성능을 보장하기 어려움.

# **Comment**
1. 다른 논문들에 비해 직관적인 observation에서 출발한 게 아주 좋았음. 실용적이며 연구적임. 훌륭한 논문이라고 생각됨.
2. 학습 데이터가 적음에도 불구하고 높은 성능을 보여주는 것은 매우 좋음.

# **Questions**
1. Pre-Train 시 사용된 데이터의 양과 종류는?
2. LiLT 모델의 학습 속도와 연산량에 대한 정보?.
3. 다른 언어로 Pre-Train한 경우의 성능 차이?.
4. BiACM 메커니즘이 다른 기존의 교차 모달리티 상호작용 방식보다 어떤 점에서 더 효과적인가?
