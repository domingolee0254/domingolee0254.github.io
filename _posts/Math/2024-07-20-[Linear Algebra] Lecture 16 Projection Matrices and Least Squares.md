---
title: "[Linear Algebra] Lecture 16 Projection Matrices and Least Squares"
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
💡

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2016%20Projection%20Matrices%20and%20Least%20Squares/Untitled.png)

</aside>

<aside>
💡 (I - P) 는 또 어디서 나오는 거야

</aside>

<aside>
💡 p에서 b는 또 어떻게 전개되는 거야

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2016%20Projection%20Matrices%20and%20Least%20Squares/Untitled%201.png)

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2016%20Projection%20Matrices%20and%20Least%20Squares/Untitled%202.png)

</aside>

<aside>
💡 왜 또 역행렬이 존재 해야하는데

![Untitled](Lhttps://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2016%20Projection%20Matrices%20and%20Least%20Squares/Untitled%203.png)

</aside>

<aside>
💡 투영벡터라는 게 정확히 무슨 의미지? aTb / aTa가 뭘 말하는거야

</aside>

투영 벡터는 한 벡터를 다른 벡터 또는 벡터 공간에 "투영"했을 때의 결과를 의미합니다. 즉, 한 벡터를 기준 벡터 또는 기준 벡터 집합에 직각으로 내렸을 때 그 교점이 투영 벡터가 됩니다. 이 개념은 특히 선형대수학에서 중요한 역할을 합니다.

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2016%20Projection%20Matrices%20and%20Least%20Squares/Untitled%204.png)

### 투영 벡터에 대한 직관적인 관점

1. 크기에 방향을 곱한 것

aTb / aTa * a⇒ aTb* a /aTa 이렇게 하면 a / aTa는 유닛벡터만 되고(방향만 정해주는 애가 되고) 두 벡터가 얼만큼 닮은지는 aTb의 내적으로 정해진다 

- ||v|| = norm2 = 크기
    - 내적을 한다는 것은 두 벡터의 를 본다는 것
    - v_hat * 크기 = V
    - 여기서 크기가 ||V||
    - 즉 v_hat = 유닛 벡터(방향만 있는)가 된다(v / ||v|| = 크기)
1. 스케일러 값으로 보는 방법
- aTb / aTa 를 스케일러 상수 C로 보면 a에 대해서 얼마만큼 곱해지는 지로 이해할 수 있다
    - C는 축소 상수