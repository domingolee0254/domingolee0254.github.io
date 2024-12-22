---
title: "[딥러닝] 1. 딥러닝은 무엇인가요?"
author_profile: false
toc: true
toc_label: "Table of Contents"
toc_icon: true
toc_sticky: true
categories:
    - Paper Review
tags:
    - Deep Learning
last_modified_at: 2024-12-23
---

# [딥러닝] 1. 딥러닝은 무엇인가요? 딥러닝과 머신러닝의 차이는?

Tags: DL
Status: Done

# 1. 정의

~~딥러닝은 “representation learning”을 포함한~~ “Artificial neural network"을 기반으로 한 "머신러닝"의 하위 분야이다. Feature engineering없이 “자동으로 데이터의 특징을 학습”하여 복잡한 문제를 해결한다.

- "Deep"이라는 표현은 네트워크에서 multiple layers를 사용하는 것을 의미
- 딥러닝은 특히 다층 신경망(Deep Neural Networks)을 활용하여 데이터로부터 "복잡한 패턴"을 학습하고, 이를 바탕으로 예측이나 분류를 수행함.
- 이 신경망은 입력 데이터를 계층적으로 처리하면서 "추상적이고 복잡한 특징"을 학습하게 됨. 예를 들어, CNN의 이미지 인식에서는 초기 층에서 단순한 선이나 모서리를 학습하고, 중간 층에서는 보다 복잡한 형상, 마지막 층에서는 전체적인 물체를 인식함.

# 2. 분류

- 머신러닝의 한 분야

![image.png](image.png)

# 3. 대조

- **Feature engineering**의 유무: 머신러닝에서는 “feature engineering”, "사람이 직접" 데이터를 분석하여 특징을 추출해야 함. 딥러닝은 이러한 과정을 오차역전파 과정을 통하여, 데이터를 입력하면 "자동으로 특징을 학습"하고 추출함.

# 질문

- 그러면 언제부터 “deep”인가?
    - 네트워크에 2개 이상의 은닉층(hidden layers)이 있을 때, 입출력 층 제외
    - 힌튼 “Deep learning”
- feature란?
    - 예측이나 분류를 할 때 사용하는 입력 데이터의 속성
- representation이란?
- 학습이란?
    
    학습이란 레이블이 있는 데이터나 레이블이 없는 데이터를 사용하여 알고리즘이 패턴을 인식하고 예측을 할 수 있도록 가르치는 과정입니다. 
    **training is the process of teaching an algorithm to recognize patterns and make predictions using labeled or unlabeled data**
    [https://www.rudderstack.com/learn/data-analytics/machine-learning-model-training/](https://www.rudderstack.com/learn/data-analytics/machine-learning-model-training/)
    
- 머신러닝에서는 백프로파게이션이 없는데 학습이라는 말을 사용할 수 있는 이유?
    - 백프로파게이션과 학습은 상관없음. 학습은 모델이 데이터들의 패턴을 찾을 수 있도록 하는 과정임.
    - 머신러닝에서는 다양한 학습 방법이 존재하며, 이 방법들은 모두 "**학습**"이라는 용어를 사용할 수 있음. 예를 들어, 회귀 분석에서 경사 하강법(Gradient Descent), 진화알고리즘.
- (위키) **backpropagation**? 머신러닝에서 역전파는 ANN의 매개변수 업데이트를 계산하도록 훈련하는 데 일반적으로 사용되는 gradient 추정 방법.
    - **In machine learning, backpropagation is a gradient estimation method commonly used for training a neural network to compute its parameter updates.**
    - 체인룰을 적용하여 마지막 층에서부터 역으로 반복하면서 계산
    - single input–output example에서 Network의 **Weight에 대한 loss funcion의 Gradient**를 계산
    - 엄밀히, **기울기를 효율적으로 계산하기 위한 알고리즘**(O), 기울기 업데이트(X)
    -