import sys
from collections import deque


def bfs():
    global directions

    queue = deque()
    day_cnt = 0 # 0으로 시작해야 1개만 익고 끝나는 날을 0으로 만들수 있음

    # 익은 토마토의 위치를 큐에 추가
    for r in range(N):
        for c in range(M):
            if tmts[r][c] == 1:
                queue.append((r, c))
                
    while queue:
        for _ in range(len(queue)):
            cy, cx = queue.popleft()
            for dy, dx in directions:
                ny, nx = cy + dy, cx + dx
                if (0<=ny<N) and (0<=nx<M) and tmts[ny][nx] == 0:
                    tmts[ny][nx] = 1
                    queue.append((ny, nx))
        if queue:
            day_cnt += 1

    # 예외처리 - (익지 않은 토마토가 있다 = 애초에 익은 토마토가 1개도 없었다 = -1 반환)
    for row in tmts:
        if 0 in row:
            return -1
                    
    return day_cnt

def main():
    global directions
    
    # visited = [[False]*M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    total_days = bfs()
    return total_days

if __name__ == "__main__":
    input = sys.stdin.readline
    M, N = map(int, input().strip().split())
    tmts = [list(map(int, input().strip().split())) for _ in range(N)]
    ret = main()
    print(ret)

# queue.append((r, c)) 왜 튜플로 넣는 거고 
# 왜 visited 행렬은 왜 없어?
# visited 행렬을 제거하고 큐에 (행, 열) 위치를 튜플로 저장하는 이유를 설명하겠습니다.
# 이유
# 큐에 (행, 열) 위치를 튜플로 저장: BFS에서 각 토마토의 위치를 추적해야 하므로, (행, 열) 좌표를 함께 저장합니다. 이는 BFS에서 일반적으로 사용하는 방식입니다. 큐에 (행, 열) 튜플을 저장하면, 나중에 큐에서 위치를 꺼내어 인접한 칸들을 쉽게 탐색할 수 있습니다.
# visited 행렬 제거: visited 행렬이 없어도 토마토가 익은 상태로 변경되었는지 여부를 tmts 행렬 자체를 통해 확인할 수 있습니다. 익은 토마토를 1로 표시하기 때문에 별도의 visited 행렬이 필요 없습니다.