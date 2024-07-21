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
last_modified_at: 2024-07-20
---

### Q1) unit vector의 정의

### Q2) 내적이 1이 된다는 것은 orthogonal의 정의지, orthonormal이기 때문에 그런것은 아니지 않나
- 아닌가 ? orthogonal은 내적이 1인 것과 상관없고 단지 내적이 0일 뿐인가

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2017%20Gram-schmidt/Untitled.png)

### Q3) orthogonal과 orthonormal의 차이?

### Q4) orthogonal M이라 하면 오소고날만 만족하는 건지 오소노말까지 돼야하는 건지

### Q5) (즁요) Q가 정방행렬일 때 P가 단위 행렬 I가 되는 이유
- 현재까지는 rectangular 형태든 square 형태를 나눠서 보는 것
- overdetermined한 직사각형인 경우에 하면, P = QQT 가 된다는 것이고
- determinded한 정사각형인 경우에 하면, P는 단순 QQT를 넘어 I 까지 간다는 것 P = QQT = I
- 왜냐하면 오버디터민드는 해가 없기 때문에 근사해를 투영행렬을 통해 얻은 것이고
- 디터민드의 경우에는 근사해를 구할 필요가 없기 때문에(이미 컬럼스페이스를 형성하는 해가 존재하기 때문에) 투영이 의미가 없어짐, 의미가 없어지려면 곱해도 그대로인 I여야함


### Q6) (중요) 그람 슈미트에서 왜 A대신 어떻게 Q를 쓸수 있다는 거지? 아예 원소가 다른 행렬인데?

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2017%20Gram-schmidt/Untitled%201.png)

### Q7) 매우 중요한 말인데 어떤 원리로 A와 Q가 컬럼 스페이스를 공유한다는 건지 이해안돼
- 그냥 Q는 A의 또다른 선형결합으로 만들어진 서브스페이스라고 하는건가
- A→Q로 갈 수 있는 이유는 그 둘이 같은 시스템이기 때문이다. = 같은 해가 나오기 때문이다
- 선형결합으로 바뀌기 때문이다
- e는 a와 b의 선형결합이어야 한다.
- p = aTb / aTa * a 투영행렬은 스케일 상수처럼 쓰여서 선형결합으로 p를 만들 수 있다.
    - 따라서 b대신 e 를 써도 된다
- e = b - p = b - (aTb / aTa * a) = b - Sa

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2017%20Gram-schmidt/Untitled%202.png)

- 그람-슈미트 과정에서 행렬 𝐴 A를 직교 행렬 𝑄 Q로 변환할 때, 𝐴 A의 열 공간(Column Space)과 𝑄 Q의 열 공간이 같은 이유는 이 과정이 각 열 벡터를 선형 변환하더라도 그들이 span하는 공간을 바꾸지 않기 때문입니다. 구체적으로 말하면, 그람-슈미트 과정은 𝐴 A의 열 벡터들을 선형 독립적이고 직교인 벡터들로 변환하는데, 이는 원래의 열 벡터들이 span하는 공간과 동일한 공간을 유지하면서, 기저 벡터들을 단순히 직교화하고 정규화하는 것입니다.

![Untitled](https://raw.githubusercontent.com/domingolee0254/domingolee0254.github.io/main/assets/image/post_image/Math/2024-07-20-%5BLinear%20Algebra%5D%20Lecture%2017%20Gram-schmidt/Untitled%203.png)


### Q8) 결국에 그람 슈미트는 왜 하는거지
- **선형 독립성과 기저 변환의 필요성**
    - 벡터 공간에서의 연산은 종종 복잡한 계산을 수반하며, 특히 비직교 벡터를 사용하면 내적, 프로젝션 등의 연산이 더 어려워집니다. 이를 해결하기 위해 벡터들을 직교화하여 계산을 단순화하고 효율적으로 만들 필요가 있었습니다.
- **정확한 계산과 수치 안정성**
    - 선형 대수학에서 정확한 계산과 수치적 안정성은 매우 중요합니다. 직교 또는 직교 정규 벡터는 수치적 안정성을 크게 향상시키며, 특히 컴퓨터를 이용한 수치 해석에서 중요한 역할을 합니다.
- **QR 분해와 같은 행렬 분해 기법의 기초**
    - 다양한 행렬 분해 기법, 특히 QR 분해는 시스템 해석, 최적화 문제 해결 등에 매우 중요합니다. QR 분해는 그람-슈미트 과정을 이용해 직교 행렬 Q와 상삼각 행렬 R을 구하는 방법 중 하나로, 이 과정이 필수적입니다.


### Q9) 결국 원래 벡터 → 그람 → 슈미트 과정은 
독립(a,b,c) → 독립 + 직교(A,B,C) → 독립 + 직교 + 정규화(q1, q2, q3) 인거 아니냐, 독립인 벡터를 독립이면서 직교이면서 정규화된 벡터로 만들어주는 과정일 뿐 아니냐
- 그람: orthogonal 구하기 위해 indepentdent 벡터에서 projection 벡터 빼줌
- 슈미트: orthonormal 구하기 위해 orthogonal 벡터에서 normalize


### Q10) QR 분해에서 R이 왜 상삼각형 꼴이냐

