import sys

def bfs(s):
    global visited, ans_bfs
    queue = []
    
    queue.append(s)
    ans_bfs.append(s)
    visited[s] = 1
    
    while queue:
        c = queue.pop(0)
        for n in adj[c]:
            if not visited[n]:
                queue.append(n)
                ans_bfs.append(n)
                visited[n] = 1
    
def dfs(c):
    global visited, ans_dfs

    ans_dfs.append(c)
    visited[c] = 1
    
    for n in adj[c]:
        if not visited[n]:
            dfs(n)
    
def main(N, M, adj):
    global visited, ans_dfs, ans_bfs
    
    visited = [0]*(N+1)
    ans_dfs = []
    dfs(V)
    
    visited = [0]*(N+1)
    ans_bfs = []
    bfs(V)
        
    return ans_dfs, ans_bfs

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, V = map(int, input().strip().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().strip().split())
        adj[s].append(e)
        adj[e].append(s)
    
    # 오름차순 정렬    
    for i in range(1, N+1):
        adj[i].sort()

    ret_dfs, ret_bfs = main(N, M, adj)
    print(*ret_dfs)
    print(*ret_bfs)
