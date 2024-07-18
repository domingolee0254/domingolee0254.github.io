import sys

def main(n):
    a = 0
    b = 1
    
    for i in range(2,91):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = b, a + b 
            if n == i:
                return b
            
if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    ret = main(n)
    print(ret)