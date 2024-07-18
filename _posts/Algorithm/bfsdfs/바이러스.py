import sys

def dfs(c):
    global ans, v
    
    ans += 1
    v[c] = 1
    
    for n in adj[c]:
        if not v[n]:
            dfs(n)
    return
    
def main(C, P, adj):
    global ans, v
    
    ans = 0
    v = [0]*(C+1)
    dfs(1)
    
    return ans-1

if __name__ == "__main__":
    input = sys.stdin.readline
    C = int(input().strip())
    P = int(input().strip())
    adj = [[] for _ in range(C+1)]
    for _ in range(P):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
        
    ret = main(C, P, adj)
    print(ret)