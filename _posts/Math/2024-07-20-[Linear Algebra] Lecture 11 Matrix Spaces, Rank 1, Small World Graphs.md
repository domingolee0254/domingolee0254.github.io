---
title: "[Linear Algebra] Lecture 11 Matrix Spaces, Rank 1, Small World Graphs"
author_profile: false
toc: false
toc_label: "Table of Contents"
toc_icon: true
toc_sticky: true
categories: 
    - Linear Algebra
tags:
last_modified_at: 2024-07-20
---

### Q1) Dimension과 rank가 정확히 어떤 대조점에서 차이가 나는 가?
- dimension: 유한 공간 R^n의 베이시스 벡터의 개수 - 벡터 스페이스 관련
- rank: 컬럼 스페이스의 차원 - 매트릭스 관련
    - 벡터안에 매트릭스가 포함되어서 헷갈리는 거, 하지만 분명 벡터 스페이스와 매트릭스는 다른 개념임
- C.Lay:
    - dimension: 유한 차원에서, 기저 벡터들의 개수를 차원
    - Rank는 A의 열공간의 차원
- 이 강의의 포인트는 매트릭스도 어떤 의미에서는 벡터 스페이스로 볼 수 있다.
- 예시) 1 4 5
           2 8 10
    - 컬럼 스페이스 차원은 1
- 랭크가 디멘션에 포함됨

### Q2) 3x3 행렬의 차원이 왜 9? basis는 9개가 필요하다?
- 3x3 행렬을 하나의 벡터라고 보는 것임
- 9개가 있어야 선형 결합해서 모든 3 by 3 매트릭스를 표현하는 기본이 되니까
- 자리에 1은 있어야 표현되니까

### Q3) 왜 S 합집합 U는 성립하지 않지?


### Q4) 왜 cos(x), sin(x)가 basis인가?
- 둘이 독립이라서 그런거야? 직교라서 그런거야?
- cos(x), sin(x)를 basis라고 가정하고, “그 성분이 얼마 만큼 있다”는 것
- sin과 cos이 하필 orthogonal한 것 ⇒ 푸리에 변환


### Q5) cos, sin 둘 다 함수인데 벡터라고 부를 수가 있나?
- cos 자체가 아니라 cos(x) 값


### Q6) 선형 독립과 직교의 정확한 차이?
- c1v1+c2v2+⋯+cnvn=0(only c_i = 0)로 보면 같은 거 아닌가?
- 애초에 개념이 다른거임, c1v1+c2v2+⋯+cnvn=0에 매몰되지 말자

#### 선형 독립(Linear Independence)

선형 독립은 벡터 집합에서 한 벡터가 다른 벡터들의 선형 결합으로 표현될 수 없는 경우를 의미합니다. 즉, 벡터들이 서로 독립적일 때, 그 어떤 벡터도 다른 벡터들의 선형 결합으로 나타낼 수 없습니다.

#### 수학적 정의

벡터 v1,v2,…,vn\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_nv1,v2,…,vn이 선형 독립이라는 것은, 다음 식을 만족하는 유일한 해가 c1=c2=⋯=cn=0c_1 = c_2 = \cdots = c_n = 0c1=c2=⋯=cn=0인 경우를 의미합니다:
c1v1+c2v2+⋯+cnvn=0c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n = \mathbf{0}c1v1+c2v2+⋯+cnvn=0

#### 직교(Orthogonality)

직교는 두 벡터가 서로 수직임을 의미합니다. 두 벡터가 직교한다는 것은 이들의 내적(스칼라 곱)이 0이라는 것을 의미합니다.

#### 수학적 정의

벡터 u\mathbf{u}u와 v\mathbf{v}v가 직교할 때:
u⋅v=0\mathbf{u} \cdot \mathbf{v} = 0u⋅v=0

#### 주요 차이점 요약

1. **정의**:
    - **선형 독립**: 벡터 집합에서 한 벡터가 다른 벡터들의 선형 결합으로 표현될 수 없는 경우.
    - **직교**: 두 벡터가 서로 수직이고, 내적이 0인 경우.
2. **조건**:
    - **선형 독립**: c1v1+c2v2+⋯+cnvn=0에서 c1=c2=⋯=cn=0인 유일한 해가 존재.
        
        c1v1+c2v2+⋯+cnvn=0c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n = \mathbf{0}
        
        c1=c2=⋯=cn=0c_1 = c_2 = \cdots = c_n = 0
        
    - **직교**: u⋅v=0.
        
        u⋅v=0\mathbf{u} \cdot \mathbf{v} = 0
        
3. **기하학적 의미**:
    - **선형 독립**: 벡터들이 서로 평면이나 공간의 다른 방향을 가리킵니다.
    - **직교**: 벡터들이 서로 90도 각도로 교차합니다.
4. **예시**:
    - **선형 독립**: 벡터 (1,0)와 (0,1)는 선형 독립입니다.
        
        (1,0)(1, 0)
        
        (0,1)(0, 1)
        
    - **직교**: 벡터 (1,0)와 (0,1)는 직교합니다.
        
        (1,0)(1, 0)
        
        (0,1)(0, 1)
        
따라서, 선형 독립과 직교는 선형대수학에서 서로 다른 관계를 설명하는 개념으로, 선형 독립은 벡터들의 의존성을 나타내고, 직교는 벡터들 간의 수직 관계를 나타냅니다.

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2011%20Matrix%20Spaces,%20Rank%201,%20Small%20World%20Graphs/Untitled.png)


### Q7) (1 5 9)와 (2 6 10)이 독립이라고 해서 (1 2 3 4)와 (5 6 7 8)도 독립이라는 보장있냐?
- (1 2 3 4)가 아니라 (2 6 10)으로 보는 건가?

### Q8) col * row 하면 rank 1 행렬이 된다는 것이 col에 대한 리니어 컴비네이션이라서 그런가?

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2011%20Matrix%20Spaces,%20Rank%201,%20Small%20World%20Graphs/Untitled%201.png)

이 행렬의 각 열(또는 행)은 c\mathbf{c}c의 상수배이므로, 이 행렬은 랭크 1입니다.

따라서, "column vector c\mathbf{c}c times row vector r\mathbf{r}r"은 일반적으로 랭크 1 행렬이 되며, 이는 c\mathbf{c}c의 한 개의 방향으로만 표현될 수 있기 때문에 그렇습니다.