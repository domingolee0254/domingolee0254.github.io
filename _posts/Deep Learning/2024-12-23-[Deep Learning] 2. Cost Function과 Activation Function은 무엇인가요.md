---
title: "[딥러닝] 2. Cost Function과 Activation Function"
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

# [딥러닝] 2. Cost Function과 Activation Function은 무엇인가요?

Tags: DL
Date: 2024년 4월 22일
Person: Domingo
Priority: Medium
Status: Done

# **1. 비용함수**

**#예측과 정답의 차이**

비용함수는 통계나 머신러닝등에서 모델의 예측값과 실제 정답의 차이를 정량화하는 함수이다. 예를 들어, mse entropy 가 있다.

- 수학이나 결정이론(가장 큰 개념에서) 등에서는 어떤 변수를 실수로 변환시켜주는 것(함수), 사건(어떤 행위나 목적)에 대한 cost가 아닌 것을 real value인 cost로 만들어주는 것
    - 최적화 과정에서, 값이나 변수들을 줄어들게 만드는 것
    - 딥러닝에서는 예측과 정답의 차이
- 목적 함수안에 cost function이 포함된다
    - 구할 값이 줄어들게 하는 목적 함수가 코스트 펑션or로스 함수
- 정답이라기 보다는 지향점, 작을 수록 좋은 경우에 정답이 있나?
- ex)  mse, x entropy

# 2. 활성화 함수

**#비선형 #노드 #복잡한 문제**

신경망에 비선형성을 추가하여, 값이 fire되도록 사용하는 함수 

- 정의상 비선형적이어야 하는 것은 아니다
- 활성화 함수 자체가 뇌에서 fire하는 것을 따라함
- 그 동작이 비선형적
    - 입력에 대해 정비례하지 않는 출력(ex. 입력의 양이 많다고 출력도 양이 많은 것은 아님)
- 복잡한 것을 표현할 수 있게 됨

ex)  시그모이드, 렐루, 겔루, 하이퍼볼릭

# 3. 렐루를 사용하는 이유

장: 하드웨어적인 장점

1. 양/음만 보면됨

- 시그모이드 탄h는 연산이 exp 등등 너무 복잡
1. 확실한 real zero가 나온다 0.000이 아니라 / 시그모이드 등은 0근처의 값들이 문제(영향은 적은데 괜히 긺  0.0001) 

단: 다잉렐루, 웨이트밸류가 음수일때 0으로 나와서

- 처음에 렐루 문제 해결하려고 웨이트 이니셜라이즈를 잘 사용함
- 하드웨어에서 계산할 때 특정 값을 추정해서 사용한다
    - 구간 정해서 0-1사이 값은 0으로 등등