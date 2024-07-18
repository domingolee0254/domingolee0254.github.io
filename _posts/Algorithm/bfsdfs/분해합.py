import sys

def main(N:int) -> int:
    for gen in range(1, N+1):
        part_sum = sum(int(digits) for digits in str(gen))
        if gen + part_sum == N:
            return gen
    return 0
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    ret = main(N)
    print(ret)