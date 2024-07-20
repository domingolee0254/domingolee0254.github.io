---
title: "[Paper] Width & Depth Pruning for Vision Transformers"
author_profile: false
toc: True	
toc_label: "Table of Contents"
toc_icon: True
toc_sticky:	True
categories: 
    - Paper Review
tags: 
    - Vision Transformers
    - Pruning
last_modified_at: 2022-07-21
---

# **Summary**

- 문제점: 기존 비전 트랜스포머 연구는 width만 고려하는 프루닝을 함.
- Key idea: width와 depth를 동시에 줄이는 프레임워크 만듦.
 - 중요/안중요한 부분을 결정하기 위한 기준을 학습 가능한 파라미터로 설정함.
- 결과: 이미지 분류와 검색 태스크에서 진행, 정확도 1% 하락 반면에 처리량은 15% 향상.   


# **Strong**

1.	프루닝 대상에 대한 기준을 정하는 아이디어가 좋았음. Linear matrix, attention head의 Learnable score를 백프로파게이션할 때 구하는 것이 좋음. 
 - 왜냐하면 다른 연구들에서도 완성된 모델에서 중요한 부분을 확인하는 것보다 이 방법이 더 정확하다고 함. 
 - 또한 헤드의 경우는 직접 지정할 수 있다고 해도 리니어 매트릭스는 특정 차원을 프루닝할 지 확인하는 것이 어려울 거기에 직접 최적화시킨 것이 적절한 방법이라고 생각함.  


# **Weakness**

1. 일반화를 하기에 실험이 부족한 것 같음. 태스크를 제한했다는 표현이 없음. 
 - 왜냐하면 효율적인 프루닝을 한다고 주장했는데, 실험 내용으로는 클래시피케이션이랑 리트리벌만 있음. 
 - 이 둘은 글로벌 도메인임. Dense prediction(segmentation)이나 local 도메인에서 하는 것들도 해야 이 프레임워크가 효율적이라는 것을 증명할 수 있을 듯.  
2. 오타가 너무 많고(“m and n being the number of output and input dimension”) 수식과 수도 코드에서 말하는 변수 값이 정확히 뭔지 이해하기 어렵게 표현함(“threshold parameter βl within (0, 1):” <->“threshold parameter βi = 10”)
 - 실험한 내용이 모티베이션을 잘 커버하는 지, 정당한지 일관된지 , 주장과 실험 내용이 맞는가


# **Comment**

1. 패치 임베딩을 줄이는 방법은 왜 적용하지 않았을까. 어텐션 연산 비용은 헤드 수가 결정적인 게 아니고 차원이 결정적이므로, 차원 자체를 줄이면 어땠을까 함.
2. depth가 중요한 이유가 궁금했는데, Width만 줄였을 때와 depth만 줄였을 때 결과의 비교가 나와있음. 같은 프루닝 비율이라면 뎁스를 줄이는 것이 더 효율적이었다는 언급이 있음.


# **Questions**

## Width pruning

- Learnable saliency score
  - Q1) S는 벡터이고 S_j ≤phi(S|m*r)이 파이의 리턴이 어떻게든 스칼라가 되어야 구조도 그림처럼 됨 
    - S_h ∈ R1 ( 어텐션 부분에서 답이 나오네 스칼라로)
  - Q2) M_j 0, 1 이라는 것은 0벡터, 1벡터 라는 것?
  - Q3) 행렬 S에서 mr 개 만큼 고를 때 열 기준으로 고르면 첫 번 째 열에서 가장 작은 mr개랑 두 번째 열에서 가장 작은 m*r 개가 같다는 보장이 어딧어? 
    - 왜 같아야만 하냐면 row 기준으로 전부 똑같이 1이나 0이 되야 하니까
  - Q4) 결국 m*r이 하는 것은 입력을 줄이는 것이냐 출력을 줄이는 것이냐
    - 코드를 보지 않으면 이해 안될듯
  - Q5) ∂aj / ∂Mj 가 왜 무시할만큼 작은 거지?
  - Q6) saliency score가 하나 구해지면 그걸로 리니어 레이어, 어텐션 레이어 전부 동일한 값을 쓰는거야? 
    - 학습 되는 것들은 score와 threshold

## Learnable threshold

  - Q7) βl within (0, 1)이라고 쳐 해놓고 왜 threshold parameter βi = 10 for each layer i 냐고 
    - 0~1사이면 시그모이드 거쳐 나온 출력은 0.5~0.7 인데 프루닝 레시오(r_l)이 이래야하는데 왜 그래프에서는 0~0.7이냐고
    - 코드에서도 그냥 torch.sigmoid()임
  - Q8) fig4에서는 한 블럭안에서 비율 다 합치면 1이고 , 각 r_l들은 레이어에 대한 비율이니까 0~1사이값인 것? 
    - 모든 r_l이 다 비율이 다른가? 다르
    - (r1, r2, ..., rL)∗ = arg minL(A(r1, r2, ..., rL))

## Depth pruning

  - Q9) 왜 our depth pruning can obtain an end-to-end pruned model, 왜 더 branchynet보다 더 좋다는 거야?
