---
title: "[Linear Algebra] Lecture 15 Projections onto Subspaces"
author_profile: false
toc: true
toc_label: "Table of Contents"
toc_icon: true
toc_sticky: true
categories: 
    - Linear Algebra
tags:
last_modified_at: 2024-07-20
---

<aside>
💡 Ax=b 에서 어떻게 최적해가 나오지?
식을 보면 이해가 되는데, 해가 없는데 무

</aside>

- determined = 조건이 있다.(방정식)
    - overdetermined 조건이 많다 = 해가 무수히 많음, 만족시킬 조건이 너무 많음- 결정 못짓게 됨
    - 그래서 구할 수 없는 b를 왜 구하려고 하느냐, 조건이 너무 많지만 그래도 모든 조건들을 최대한 만족시켜보자
    - 애초에 왜 구하냐, 애초에 구하려고 조건들을 모았는데 그게 너무 많다는 것
    - A의 컬럼 스페이스 = 가장 이상적인 조건들을 만족하는 공간이됨(유클리디안)
- 근사값을 구하는

<aside>
💡 이 경우~ 컬럼 벡터의 차원이 
뭔말이야

</aside>

<aside>
💡 ATA가 full rank라면 역행렬이 존재, 왜?

</aside>

- ru 분해 단원에서 A → U → RREF → I 만들엊 줄 때 E21E32E31 이런식으로 행 연산해줬잖음, 그 행 연산 자체가 A의 역행렬임
AA-1 = I 니까, 단위행렬이라는 건 ATA이 full rank여야 한다는 것(단위 행렬은 각 rref 된 위아래 다 0인 피벗들이 꽉차 있다는 거잖음) 그니까 full rank라는 거지

<aside>
💡 Full rank란?

</aside>

- 행렬 A의 랭크가 min(m,n)과 같다는 것은, 랭크가 행과 열의 개수 중 작은 값과 같다

<aside>
💡 Ax=b 에서 어떻게 최적해가 나오지?
식을 보면 이해가 되는데, 해가 없는데 무슨 확률 분포로 추정치를 추정하는 것도 아니고 전치랑 역행렬만 이용했는데 추정치가 나오는 게 이해가 안가네 신기하면서

</aside>

---

# Lecture 15

<aside>
💡 projection 단원이 왜 필요하지?

</aside>

- Ax = b를 못 구하니까 근사값을 구하는 것
- overdetermined의 경우에, Ax는 col space에 존재하지만 b는 존재하지 않음, 그래서 b는 Ax가 만든 평면에 존재하지 않아서, 평면에 존재하는 벡터들중에서 b에 가장 가까운(=수직인) 벡터를 찾아서 추정치x를 구하는 것임
- b를 a에 투영

<aside>
💡 A에 곱해진 그 벡터 x가 A의 col space에 안착한다?

</aside>

- x가 곱해지면 선형결합으로 → b가 컬럼스페이스 평면에 포함된다는 것

<aside>
💡 P^2 = P의 의미? P제곱에 b를 왜 곱해?

</aside>

- Pb=p해서 투영한 애(p)를 반복해서 투영하면 또 그자리에 p가 된다는 것

<aside>
💡 e=b-Ax_hat이 left null space에 존재한다는 게 중요한가?
A의 컬럼 스페이스와 직교한다는 게 중요?

</aside>

- p와 e가 직교한다는 의미, 투영된 벡터 p와 e로 모든 공간 표현가능.
- 다시 좀 명확히 할것- 에러벡터는 left null space에 존재하는

<aside>
💡 A,나 x를 구하는게 목표가 아니라 projection matrix P를 구하는 게 목적임(A와 x_hat을 이용해서)

</aside>