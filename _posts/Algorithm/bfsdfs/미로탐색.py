import sys
from collections import deque

def bfs(y: int, x: int, maze: list) -> int:
    global visited, directions, dist
    
    queue = deque([(y, x)])

    dist[y][x] = 1  # 시작 지점도 포함하여 1로 설정
    visited[y][x] = True
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N) and (0 <= nx < M) and maze[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
                
    return dist[N-1][M-1]

def main(N: int, M: int, maze: list) -> int:
    global visited, directions, dist
    
    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[0]*M for _ in range(N)]
    
    return bfs(0, 0, maze)

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    ret = main(N, M, maze)
    
    print(ret)



##################################################################
# sol 1
##################################################################

# import sys

# def dfs(y:int, x:int, cnt:int, maze:list) -> int:
#     global visited, directions

#     for dy, dx in directions:
#         ny, nx = y + dy, x + dx
#         if (0<=ny<N) and (0<=nx<M) and maze[ny][nx] == 1 and not visited[ny][nx]:
#             visited[ny][nx] = True
#             cnt += 1 
#             cnt = dfs(ny, nx, cnt, maze)
#     return cnt
    
# def main(N:int, M:int, maze:list) -> list:
#     global visited, directions
    
#     visited = [[False]*M for _ in range(N)]
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     cnt = 1
#     visited[0][0] = True
    
#     return dfs(0, 0, cnt, maze)

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]
#     print(maze)
#     ret = main(N, M, maze)
    
#     print(ret)