---
title: "[Linear Algebra] Lecture 14 Orthogonal Vectors and Subspaces"
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

### Q1) 직교와 독립의 차이
- 애초에 개념이 다른거임, c1v1+c2v2+⋯+cnvn=0에 매몰되지 말자
- jyp : 둘은 그냥 아예 다른 개념임
- 내적 : [x_1, x_2, x_3, … , x_n][y_1, y_2, y_3, … ,y_n]^T = x_1y_1 + x_2y_2 + … +x_ny_n
    - x_1, y_1은 벡터가 아니라 컴포넌트다(스케일러값)
- 직교: c1x_1+…+cnx_n
    - x_1, x_n들은 벡터다. 컴포넌트가 아니라.


### Q2) 왜 column space와 Left null space가 직교하는가? null space가 아니라
### Q3) 두 스페이스 S와 T가 직교하려면 0벡터에서만 만나야 하는 이유?
- 한 스페이스의 벡터가 다른 스페이스의 모든 벡터에 직교하는 점은 0벡터 뿐이라서?


### Q4) 내적 - norm - 코사인 1법칙 - 2법칙 증명 매우 중요
- 삼각 함수 정리
- 코사인 법칙들 정리
- norm의 의미 정리
- 내적vs외적 정리(직각삼각형vs평행사변)


### Q5) 내적이 두 벡터 u*v=0 인데. (두 벡터를 norm한 ||u|| * ||v|| = 0 이 아니라) 
어떻게 두 동일한 벡터이면 1이 나오지?
ex) [1 2 3]*[1 2 3]^T 하면 14잖아
- 둘이 내적한 답이 1이 아니라 cos세타 값이 1이라고 두 벡터가 동일 선상에 잇으니까 각이 세타 값이 0이라 cos세타는 1이라고
- ex) [1 2 3]*[1 2 3]^T 하면 14잖아 = > 그럼 둘이 직교가 아니겠지

### Q6) row space의 선형 결합이라는 게 와 닿지 않음, 컬럼으로 이해하면 쉬운데
- row pic → equation이다, 해들을 이은 선이다. 선 자체가 해들의 집합
- col pic → 벡터의 크기와 방향을 표현