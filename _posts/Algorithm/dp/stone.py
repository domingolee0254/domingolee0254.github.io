import sys

def main(N:int) -> str:
    dp = [False] * (N + 1)
    
    if N >= 1:
        dp[1] = True  # 1개 남으면 상근이 이김
    if N >= 2:
        dp[2] = False # 2개 남으면 창영이 이김
    if N >= 3:
        dp[3] = True  # 3개 남으면 상근이 이김
    
    # DP 테이블 채우기
    for i in range(4, N + 1):
        # 현재 돌이 i개 남았을 때
        # 상근이가 이기기 위한 조건은 (i-1)개 또는 (i-3)개의 돌이 남았을 때 창영이가 이기는 상태여야 함
        # 즉, dp[i-1]이 False이거나 dp[i-3]이 False이어야 상근이가 이길 수 있음
        if not dp[i - 1] or not dp[i - 3]:
            dp[i] = True  # 하나라도 창영이가 이기는 상태라면 상근이가 이길 수 있음
        else:
            dp[i] = False # 둘 다 상근이가 이기는 상태라면 창영이가 이김
    
    return "SK" if dp[N] else "CY"
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    ret = main(N)
    print(ret)