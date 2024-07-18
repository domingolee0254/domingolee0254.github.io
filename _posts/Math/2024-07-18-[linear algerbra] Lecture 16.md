---
title: "Lecture 16"
author_profile: false
toc: true
toc_label: "Table of Contents"
toc_icon: true
toc_sticky: true
categories: 
    - Linear Algebra
tags:
    - Projections
last_modified_at: 2024-07-18
---

# Lecture 16

**상태:** 작성 전  
**생성 일시:** 2024년 7월 7일 오전 2:16  
**수업일:** 2024년 7월 1일  
**업로드:** No  
**유형:** 수업

## Intro

<aside>
💡
</aside>

<aside>
💡 (I - P) 는 또 어디서 나오는 거야
</aside>

<aside>
💡 p에서 b는 또 어떻게 전개되는 거야
</aside>



<aside>
💡 왜 또 역행렬이 존재 해야하는데
</aside>


<aside>
💡 투영벡터라는 게 정확히 무슨 의미지? aTb / aTa가 뭘 말하는거야
</aside>

투영 벡터는 한 벡터를 다른 벡터 또는 벡터 공간에 "투영"했을 때의 결과를 의미합니다. 즉, 한 벡터를 기준 벡터 또는 기준 벡터 집합에 직각으로 내렸을 때 그 교점이 투영 벡터가 됩니다. 이 개념은 특히 선형대수학에서 중요한 역할을 합니다.


### 투영 벡터에 대한 직관적인 관점

1. **크기에 방향을 곱한 것:**

    \[
    \frac{a^T b}{a^T a} \cdot a \Rightarrow \frac{a^T b}{a^T a} \cdot a
    \]

    이렇게 하면 \(\frac{a}{a^T a}\)는 유닛벡터가 되고(방향만 정해주는 역할을 하며) 두 벡터의 유사성은 \(a^T b\)의 내적으로 정해집니다.

    - ||v|| = norm2 = 크기
    - 내적을 한다는 것은 두 벡터의 유사성을 본다는 것
    - \(v_{\hat{v}} \cdot\) 크기 = V
    - 여기서 크기가 ||V||
    - 즉 \(v_{\hat{v}}\)는 유닛 벡터(방향만 있는 벡터)가 됩니다(\(\frac{v}{||v||}\) = 크기).

2. **스케일러 값으로 보는 방법:**

    - \(\frac{a^T b}{a^T a}\)를 스케일러 상수 C로 보면 a에 대해 얼마만큼 곱해지는지를 이해할 수 있습니다.
    - C는 축소 상수입니다.

이 내용을 바탕으로 투영 벡터의 개념을 이해할 수 있습니다.
