---
title: "[Linear Algebra] Lecture 12 Graphs, Networks, Incidence Matrices"
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

### Q1) 컬럼으로 보면 → 한 노드 에서 나가는 모든 양
로우로 보면 → 어디서 나가서 어디로 들어가는 지 양

### Q2) 로우 스페이스랑 널 스페이스랑 직요하는데 컬럼스페이스에 A곱하는데 어떻게 널스페이스야?
### Q3) loop와 edge
### Q4) Null space of A에서 [c c c c]에 의해 한번에 전류가 결정된다는 게 한번에 C만큼 전류를 주면 전류가 그렇게 된다는 건지(근데 전류가 흐르지 않는다고 햇는데 무슨말이지)
- 널스페이스의 베이시스 = [1 1 1 1] → 상수배c를 해도 전부

# 참고

- Kirchhoff CL(LNS) / VL(Null space)
    - KVL = 내가 원래의 위치 까지 한바퀴돌면 전위차 전압은 0이다.
    - null space 구하는 과정은 회로니까 전부합은 0 인데, 각각의 노드가 몇 볼티지였을까 찾는거 = 해
- 전압 = 전위차(어디를 기준으로 했는지 가 중요 - 지면)
    - 전하 = 질량
    - 전자기력 = 중력
    - 전위차 = 높이(위치 차이)