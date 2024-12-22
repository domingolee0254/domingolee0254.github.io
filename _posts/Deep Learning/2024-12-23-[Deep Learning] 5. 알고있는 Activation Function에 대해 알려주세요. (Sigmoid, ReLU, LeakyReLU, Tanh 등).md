---
title: "[딥러닝] 5. Activation Function에 대해 알아보기"
author_profile: false
toc: true
toc_label: "Table of Contents"
toc_icon: true
toc_sticky: true
categories:
    - Deep Learning
tags:
    - Deep Learning
last_modified_at: 2024-12-23
---

# [딥러닝] 5. 알고있는 Activation Function에 대해 알려주세요. (Sigmoid, ReLU, LeakyReLU, Tanh 등)

Status: In progress

### Sigmoid → ReLU → Leaky ReLU

- 각각의 문제와 해결

# 1. Sigmoid Function

- **수식**:

$$
\text{Sigmoid}(x) = \frac{1}{1 + e^{-x}} 
$$

- **특징**:
    - 출력 범위: (0, 1)
    - 이진 분류 문제에서 주로 사용
- **장점**:
    - 모든 입력을 확률로 해석 가능
- **단점**:
    - 입력 값이 크거나 작을 때 기울기가 0에 가까워지는 `saturation` → Gradient Vanishing 문제
    - Non-zero-centered Output → 입력값의 부호에 그대로 영향받음 → Gradient Descent시 zigzag
    

# 2. ReLU (Rectified Linear Unit)

- **수식**:

$$
\text{ReLU}(x) = \max(0, x)

$$

- **특징**:
    - 입력이 0보다 크면 그 값을 그대로 출력, 0 이하면 0 출력
    - 현재 가장 널리 사용되는 활성화 함수
- **장점**:
    - 계산이 빠르고 효율적
    - 양의 입력 ⇒ `saturation` 문제 없음 → 기울기 소실 문제 감소
- **단점**:
    - 음의 입력 ⇒ 어떤 업데이트도 되지 않는 Dying ReLU 문제 (음수 입력에서 뉴런이 비활성화되는 문제)
    

# 3. Leaky ReLU

- **수식**:

$$
\text{Leaky ReLU}(x) =
\begin{cases}
x & \text{if } x > 0 \\
\alpha x & \text{if } x \leq 0
\end{cases}  
$$

(여기서 α\alphaα는 작은 상수, 예: 0.01)

- **특징**:
    - ReLU의 변형, 음수 입력에 대해 작은 기울기 부여
- **장점**:
    - 음수 입력 ⇒ 0이 아니게 됨 → Dying ReLU 문제 완화
- **단점**:
    - α\alphaα 값 선택이 중요
    

# 4. Tanh (Hyperbolic Tangent)

- **수식**:

$$
\text{Tanh}(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} 
$$

- **특징**:
    - 출력 범위: (-1, 1)
    - Sigmoid와 유사하지만, 0을 중심으로 대칭적
- **장점**:
    - 출력이 0을 중심으로 하여, 가중치 업데이트가 효율적
- **단점**:
    - 입력 값이 크거나 작을 때 기울기가 0에 가까워지는 `saturation` → Gradient Vanishing 문제
    

### 활성화 함수 선택 가이드

- **ReLU**: 기본 선택. 대부분의 상황에서 좋은 성능.
- **Leaky ReLU**: ReLU의 Dying ReLU 문제를 개선한 버전.
- **Tanh**: 출력이 -1과 1 사이에서 대칭적 분포를 가질 때 유리.
- **Sigmoid**: 주로 출력층에서 이진 분류를 위한 활성화 함수로 사용.