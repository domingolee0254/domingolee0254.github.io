---
title: "[Linear Algebra] Lecture 10 The Four Fundamental Subspaces"
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
💡 왜 row space와 col space의 차원이 항상 같지?

</aside>

- row로 보나 col로 보나 같은 시스템이라 col로 봤을 때 부정이었던 게 row로 본다고 해가 생기는 것은 아니니까
- 그래도 이해안되는 걸?
- pivot의 개수: 공간을 정의하는 요소의 개수, 시스템이 정해지면 row의 피봇의 개수나 col의 피봇의 개수나 그냥 같은 거임
- pivot의 정의상 행으로 보나 열로 보나 1이 있는게 1개임

<aside>
💡 행렬 A의 row space의 basis는 R 행렬의 처음 r개의 row vector들
원리가 이해 안됨

</aside>

- pivit의 관점으로 보면, 행/열로 보나 정의상 그 행/열에서 1개임
    - pivot은 무조건 column을 말함
    - pivot을 남기려고 reduce함 → 독립적인 row만 남음

<aside>
💡 A의 row space의 차원? A의 rank가 row space의 차원?

</aside>

<aside>
💡 Rank, component, dimension 개념 정확히 하기

</aside>

<aside>
💡 왜 left null space에서 rank가 m-r이지?


</aside>
![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/%5BLinear%20Algebra%5D%20Lecture%2010%20The%20Four%20Fundamental%20Subspaces/leftnullspace.png)

- A에서 row 개수인 m은 A^T에서 col 개수가 됨
    - m-r = A^T의 free col 개수 =A^T null space의 차원
    

<aside>
💡 X_comp = x_part + x_null 일 때 particular 해가 컬럼 스페이스에 존재하는 거 아니었어?
col space와 nullspace를 모두 합치면 모든 R^n 공간 표현한다는 거 같은데 결국 x_parti가 row space 인지 col space인지

</aside>

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/%5BLinear%20Algebra%5D%20Lecture%2010%20The%20Four%20Fundamental%20Subspaces/foursubspaces.jpg)

- 이 그림을 설명할 줄 알아야 함
1. Ax=0 / Ax ≠0인 경우 나눈 것
2. A = 선형 결합 그자체  = mapping function의 관점
3. col space가 위치한 곳
    - x 가 아니라 A가 선형 결합으로 만들 수 있는 공간
4. free, pivot col 관점
    - pivot basis는 2개 → 2개가 만드는 공간은 평면
- 왜 dim이 r로 같지?
- pivot vs basis
- rank vs dimension


