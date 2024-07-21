---
title: "[Linear Algebra] Lecture 18 Properties of Determinants"
author_profile: false
toc: False
toc_label: "Table of Contents"
toc_icon: true
toc_sticky: true
categories: 
    - Linear Algebra
tags:
last_modified_at: 2024-07-21
---

### Q1) prop 4) 같은 row가 이미 2개라서 det이 0이 된다는 거랑, 같은 row를 행교환했을 때 det이 0이 되어야만 prop2가 만족한다는 게 무슨 연관임?
- det을 구하는 과정에 행교환이 없지않음? 그냥 ad-bc아님?

- 성질 자체는 prop 4 그 자체를 말하는 것임
    - 동일한 row가 있다면, 그냥 det = 0이라는 건데 그것을 설명하려고 prop2를 가져와서 설명함
- 같은 행렬인데 행만 바꿨다고 det이 바뀔 수 없잖음

### Q2) 특이행렬(singular matrix)이란?

- 역행렬이 존재하지 않는 행렬
- 정확히 왜 singular라는 말을 사용했지는 지는 모르겠음
1. inverse가 없기 때문에 (invertible)(inverse) 짝이 아니어서
2. 수학에서 single은 특별, 동작이 제대로 되지 않는, 일반적이지 않은, 이례적인, 예외적인 것을 말함
    1. 역원, 항등원이 존재하는 것이 일반적인데(행렬도 역행렬이 있는게 일반적) 없기 때문에 특이 아닐까

### Q3) Prop 3에서 모든 row에 동시에 선형적이지 않다?

- “하나의 row에 대해서만 선형적” (상수 배든, row 덧셈 연산이든 간에)
    - scale 상수배(prop 3-1)과 행렬곱은(prop 9) 아예 다른 개념임. 행렬곱에 닫혀있다고 상수배도 된다는 게 아님

### Q4) Prop 6에서 0으로된 row가 존재하면 rank가 n보다 작아진다?

- 현재까지는 square matrix를 다룬다(전제) ⇒ determined matrix = sqaure
- row가 0이 된다 = equation이 0이 된다 = 해를 만족하는 조건이 0 이 되었다 = pivot이 0이 되었다 ⇒ column space를 만들 수 있는 벡터가 삐꾸가 되었다 = b로 span이 불가능 하다
- column이 하나 없어졌다 = Full rank가 아니게 된다 = rank < n이 된다 ⇒ col space에 b가 올라갈 수 없는 경우가 발생