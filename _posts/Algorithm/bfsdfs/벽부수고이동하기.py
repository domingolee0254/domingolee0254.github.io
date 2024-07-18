import sys
from collections import deque

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향 정의
    queue = deque([(0, 0, 0)])  # (y, x, wall_broken) 형태로 큐 초기화
    visited[0][0][0] = True  # 시작점 방문 표시
    distance = 1  # 초기 거리

    while queue:
        for _ in range(len(queue)):
            y, x, wall_broken = queue.popleft()

            # 목표 지점 도달 시 거리 반환
            if y == N - 1 and x == M - 1:
                return distance

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < M:
                    # 벽이 없고 방문하지 않은 경우
                    if maps[ny][nx] == 0 and not visited[ny][nx][wall_broken]:
                        visited[ny][nx][wall_broken] = True
                        queue.append((ny, nx, wall_broken))
                    # 벽이 있고 벽을 부순 적이 없는 경우
                    elif maps[ny][nx] == 1 and wall_broken == 0 and not visited[ny][nx][1]:
                        visited[ny][nx][1] = True
                        queue.append((ny, nx, 1))
        distance += 1  # 모든 방향 탐색 후 거리 증가

    return -1  # 목표 지점에 도달할 수 없는 경우 -1 반환

def main():
    global visited, maps, N, M

    # 방문 여부를 저장할 3차원 리스트 초기화
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]

    return bfs()

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())  # 행렬 크기 입력
    maps = [list(map(int, input().strip())) for _ in range(N)]  # 맵 정보 입력
    result = main()
    print(result)  # 결과 출력