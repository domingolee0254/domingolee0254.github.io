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
- Problem:
  - 기존 모델들은 대부분 특정 1가지 언어로 된 문서로만 학습하는 것에 초점을 맞춤.
    - 프리트레인 데이터가 부족한 언어의 문서일 경우 학습하기 어려움.
    - 여러 언어를 처리하는 경우 문제가 발생함.

- Goal
  - 특정 언어에 국한되지 않는 문서 형태 처리 모델 및 학습 방법 제안.

- Observation
  - 문서의 형태(layout)가 동일하다면, 그 문서의 언어(language)가 바뀌어도 의미 파악이 쉬움.

<img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/01.observation.jpg" alt="Untitled">

- Key idea:
  - 텍스트와 레이아웃 부분을 '구분', '분리'하여 처리할 수 있는 트랜스포머 구조 제안.
  - 문서의 형태가 동일하면 언어가 달라도 의미 파악이 용이함.

<img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/02.architecture.jpg" alt="Untitled">

- Result:
  - Pre-train시 비교적 부족한 문서 데이터로도 높은 성능 달성
  - 영어, 중국어, 불어 등 여러 언어에 대한 실험 결과는 기존 SOTA 모델에 비해 F1 스코어 0.02 상승.

# **Strong**
1. LiLT 모델은 기존 Sota 모델에 비해 적은 데이터로 학습함에도 가장 높은 성능을 보여줌.

2. 영어로만 Pre-Train되었음에도 불구하고 중국어를 비롯한 모든 언어에서 가장 높은 성능을 보여줌.
  <img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/06.FT_res.jpg" alt="Untitled">
  - (다국어 언어 데이터에서) 영어로 Pre-Train되었음에도, 다국어로 학습된 SOTA 모델과 비슷하거나 높은 성능.
  <img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/07.SER.jpg" alt="Untitled">
  <img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/08.SER2.jpg" alt="Untitled">
  - (단일 언어 데이터에서도) 단일 중국어, 영어 모델 또는 다국어 모델과 결합한 릴트가 다국어로 프리트레인된 모델보다 뛰어난 성능을 보여주면서 타언어를 비롯한 *다국어 모델(infoxlm)과 높은 호환이 됨.

3. BiACM 메커니즘을 통해 언어 독립적인 교차 모달리티 상호작용을 강화함.
  - 비동기 최적화 전략을 사용하여 텍스트와 레이아웃 흐름을 효과적으로 분리하고 결합함.
  - 이것은 글과 문서 형태 정보의 분리(Pre-Train 시)와 결합(Fine-tuning 시)이라는 학습 방법의 유효함을 보여줌.
  - BiACM의 핵심은 detach였음.
<img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/03.formula.jpg" alt="Untitled">

# **Weakness**
1. 'language-independent'모델이라는 메인 주장을 하기에 실험이 부족한 것 같음.

# **Comment**
1. 다른 논문들에 비해 직관적인 observation에서 출발한 게 아주 좋았음.
  - 영어보다 확연히 부족한 언어로 된 문서에 적용할 수 있다는 점에서 실용적이며 연구적임. 훌륭한 논문이라고 생각됨.

2. 학습 데이터가 적음에도 불구하고 높은 성능을 보여주는 것은 매우 좋음.

# **Questions**
1. 최적화 속도 면에서, Pre-train시의 Text flow의 최적화 속도를 늦추는 이유?
  - Pre-train된 언어 모델 사용 => 어느정도 이미 최적화 + 모델의 학습을 늦추기로 함.
  - Text -> Layout: 작은 그래디언트 => 언어 정보와 함께 ‘형태’ 학습 => 적은 그래디언트가 흘러 ‘형태’를 배우는 부분이 ‘글’을 학습하는 부분에 과적합되는 것을 방지.
  - Layout -> Text: 큰 그래디언트 발생, Text 모델로 흐르는 것을 차단, ‘글’을 학습하는 부분이 ‘형태’를 배우는 부분에서 분리되어 학습.
  - 최적화 속도를 개선하기 위해 텍스트 모델의 파라미터를 작은 단위로 변경하는 방법이 적용됨. 이는 두 모델 간의 그래디언트 크기 차이를 고려하여, 텍스트 모델이 이미 어느 정도 최적화된 상태에서 레이아웃 모델에 의해 너무 많이 영향을 받지 않도록 하기 위한것으로 생각됨. 작은 그래디언트 변경은 텍스트 모델이 레이아웃 모델에 과적합되는 것을 방지하기 떄문.

2. 중국어로 Pre-Train한 경우에는 어떻게 될까?.
  - 논문에서는 언어 독립적 레이아웃을 주장하며, 영어로 Pre-train된 모델이 중국어 데이터에서 더 높은 성능을 보였음. 이 결과로 미루어 보아, 중국어로 Pre-train된 모델이 영어와 같은 다른 언어 데이터에서도 유사하게 높은 성능을 보일 수 있는지 실험해 봐야 주장한 대로 'language-independent'한 모델을 증명할 수 있지 않을까함.

3. Table 6에서 어떻게 영어로 pt한 모델이 ft한 후에도 영어보다 중국어 성능이 더 높을 수 있을까?
  <img src="https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Paper Review\2024-07-21-[Paper] LiLT A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding/09.FT_res_comments.jpg" alt="Untitled">
  - 언어의 특성 차이에서 기인할 수 있다고 생각함. 중국어는 한자 계열의 표의문자로 각 문자가 독립적인 의미를 가지며, 이는 모델이 더 문맥에 상관없이 명확한 의미 파악을 용이함. 반면, 영어는 표음문자로, 같은 단어가 문맥에 따라 다양한 의미를 가질 수 있어 학습이 더 복잡할 수 있음.
  - 같은 의미에서 한국어에 이 논문을 적용한다면, 중국어보다는 낮고 영어랑 비슷한 성능이 나올 것으로 예상함.
  - 아랍어 같은 경우는 오른쪽에서 왼쪽으로 읽으므로, text보다 layout에 더 영향을 많이 받으므로

4. 연산량과 레이턴시에 대한 추가 연구가 필요할 듯?
  - 실제로 대규모 문서를 처리할 때 모델의 연산량과 레이턴시는 매우 중요한 요소임. 모델이 실용적으로 사용되기 위해서는 높은 처리 속도와 효율적인 연산량 관리가 필수적. 따라서, 모델의 실제 적용 가능성면에서 연구해 볼 필요가 있겠음.
    - 참고 Donut

5. Pre-Train 시 사용된 데이터의 양과 종류는?
  - InfoXLM에 있음. 30M개의 데이터이며, 수십여?가지 언어들이 있었음. 데이터 분포는 영어가 압도적으로 많고 다른 언어들은 기하급수적으로 적어짐.

6. BiACM 메커니즘이 다른 기존의 교차 모달리티 상호작용 방식보다 어떤 점에서 더 효과적인가?
  - cross-attention과 비교한 것이 있음. Co-attention에 비해 동일한 연산량, 단순한 과정, 더 높은 성능 => 효율적 구조

# **References**
[1] Wang, Jiapeng, Lianwen Jin, and Kai Ding. "Lilt: A simple yet effective language-independent layout transformer for structured document understanding." *arXiv preprint* arXiv:2202.13669, 2022.

[2] Lin, Weihong, et al. "ViBERTgrid: a jointly trained multi-modal 2D document representation for key information extraction from documents." *Document Analysis and Recognition–ICDAR 2021: 16th International Conference, Lausanne, Switzerland, September 5–10, 2021, Proceedings, Part I* 16. Springer International Publishing, 2021.

[3] Xu, Yiheng, et al. "Layoutxlm: Multimodal pre-training for multilingual visually-rich document understanding." *arXiv preprint* arXiv:2104.08836, 2021.

[4] Lu, Jiasen, et al. "Vilbert: Pretraining task-agnostic visiolinguistic representations for vision-and-language tasks." *Advances in neural information processing systems* 32, 2019.

[5] Park, Seunghyun, et al. "CORD: a consolidated receipt dataset for post-OCR parsing." *Workshop on Document Intelligence at NeurIPS*, 2019.

[6] 오수지, 고려대학교 산업경영공학부 DSBA 연구실, [Paper Review] LayoutLM from V1 to V3 (LayoutLM, LayoutLMv2, LayoutLMv3), <https://www.youtube.com/watch?v=3yOQXVUJ6h8>, 2023.

[7] <https://hsleeword.wordpress.com/2022/04/19/lilt-a-simple-yet-effective-language-independent-layout-transformer-for-structured-document-understanding/>, 2022