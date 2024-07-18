import sys

def dfs(y, x, carb_loc, warms):
    global visited, directions  
    #global visited, directions, warms # 체크1: warms를 전역으로 하면 중복으로 더해짐

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if (0<=ny<N) and (0<=nx<M) and carb_loc[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            warms += 1
            dfs(ny, nx, carb_loc, warms)

    return warms



def main(N:int, M:int, K:int, carb_loc:list) -> int:
    
    global visited, directions
    warms = 0
    visited = [[False]*M for _ in range(N)]
    directions = [(-1, 0),(1, 0), (0, -1), (0, 1)]

    for r in range(N): # r == y
        for c in range(M): # c == x
             if carb_loc[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True # 갔으면 일단 찍음, 갔으면 일단 1마리 씀
                warms += 1
                dfs(r, c, carb_loc, warms)

    return warms
    
if __name__ == "__main__":
    sys.setrecursionlimit(10**6) # 체크2: 이거 없으면 에러남
    input = sys.stdin.readline
    T = int(input().strip())
    results = []
    for t in range(T):
        N, M, K = map(int, input().strip().split())
        carb_loc = [[0]*M for _ in range(N)]
        for k in range(K):
            X, Y = map(int, input().strip().split())
            carb_loc[X][Y] = 1
        
        ret = main(N, M, K, carb_loc)
        results.append(ret)
    for res in results:
        print(res)
