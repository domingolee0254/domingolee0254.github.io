import sys

def dfs(y, x, maps, cnt):
    global visited, directions
    
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if (0<=ny<N) and (0<=nx<M) and maps[ny][nx] == 1 and not visited[ny][nx]:
            cnt += 1
            visited[ny][nx] = True
            cnt = dfs(ny, nx, maps, cnt)
    
    return cnt
        
def main(maps):
    global visited, directions
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    cnt_list = []
    for n in range(len(maps)):
        for m in range(len(maps[0])):
            if maps[n][m] == 1 and not visited[n][m]:
                cnt = 1
                visited[n][m] = True
                cnt = dfs(n, m, maps, cnt)
                cnt_list.append(cnt)
    return max(cnt_list)

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N, M, K = map(int, input().strip().split())
    maps = [[0]*M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().strip().split())
        maps[r-1][c-1] = 1
    ret = main(maps)
    print(ret)
    