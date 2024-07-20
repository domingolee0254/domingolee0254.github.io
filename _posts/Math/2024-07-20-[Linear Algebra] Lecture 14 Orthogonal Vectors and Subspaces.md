---
title: "[Linear Algebra] Lecture 14 Orthogonal Vectors and Subspaces"
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
💡 직교와 독립의 차이

</aside>

- 애초에 개념이 다른거임, c1v1+c2v2+⋯+cnvn=0에 매몰되지 말자

### 선형 독립(Linear Independence)

- 선형 독립은 벡터 집합에서 한 벡터가 다른 벡터들의 선형 결합으로 표현될 수 없는 경우를 의미합니다. 즉, 벡터들이 서로 독립적일 때, 그 어떤 벡터도 다른 벡터들의 선형 결합으로 나타낼 수 없습니다.
- 벡터 v1,v2,…,vn이 선형 독립이라는 것은, 다음 식을 만족하는 유일한 해가 c1=c2=⋯=cn=0인 경우를 의미

### 직교(Orthogonality)

- 직교는 두 벡터가 서로 수직임을 의미합니다. 두 벡터가 직교한다는 것은 이들의 내적(스칼라 곱)이 0이라는 것을 의미합니다.
- 벡터 u와 v가 직교할 때:
u⋅v=0

### 주요 차이점

1. **정의**:
    - **선형 독립**: 벡터 집합에서 한 벡터가 다른 벡터들의 선형 결합으로 표현될 수 없는 경우.
    - **직교**: 두 벡터가 서로 수직이고, 내적이 0인 경우.
2. **기하학적 의미**:
    - **선형 독립**: 벡터들이 서로 평면이나 공간의 다른 방향을 가리킵니다.
    - **직교**: 벡터들이 서로 90도 각도로 교차합니다.
3. **예시**:
    - **선형 독립**: 벡터 (1,0)와 (0,1)는 선형 독립입니다.
        
        (1,0)(1, 0)
        
        (0,1)(0, 1)
        
    - **직교**: 벡터 (1,0)와 (0,1)는 직교합니다.
        
        (1,0)(1, 0)
        
        (0,1)(0, 1)
        

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2014%20Orthogonal%20Vectors%20and%20Subspaces/Untitled.png)

### jyp

둘은 그냥 아예 다른 개념임

- 내적 : [x_1, x_2, x_3, … , x_n][y_1, y_2, y_3, … ,y_n]^T = x_1y_1 + x_2y_2 + … +x_ny_n
    - x_1, y_1은 벡터가 아니라 컴포넌트다(스케일러값)
- 직교: c1x_1+…+cnx_n
    - x_1, x_n들은 벡터다. 컴포넌트가 아니라.

<aside>
💡 왜 column space와 Left null space가 직교하는가? null space가 아니라

</aside>

<aside>
💡 두 스페이스 S와 T가 직교하려면 0벡터에서만 만나야 하는 이유?

</aside>

- 한 스페이스의 벡터가 다른 스페이스의 모든 벡터에 직교하는 점은 0벡터 뿐이라서?

<aside>
💡 내적 - norm - 코사인 1법칙 - 2법칙 증명 매우 중요
- 삼각 함수 정리
- 코사인 법칙들 정리
- norm의 의미 정리
- 내적vs외적 정리(직각삼각형vs평행사변)

</aside>

<aside>
💡 내적이 두 벡터 u*v=0 인데. (두 벡터를 norm한 ||u|| * ||v|| = 0 이 아니라) 
어떻게 두 동일한 벡터이면 1이 나오지?
ex) [1 2 3]*[1 2 3]^T 하면 14잖아

</aside>

- 둘이 내적한 답이 1이 아니라 cos세타 값이 1이라고 두 벡터가 동일 선상에 잇으니까 각이 세타 값이 0이라 cos세타는 1이라고
- ex) [1 2 3]*[1 2 3]^T 하면 14잖아 = > 그럼 둘이 직교가 아니겠지

<aside>
💡 row space의 선형 결합이라는 게 와 닿지 않음, 컬럼으로 이해하면 쉬운데

</aside>

- row pic → equation이다, 해들을 이은 선이다. 선 자체가 해들의 집합
- col pic → 벡터의 크기와 방향을 표현