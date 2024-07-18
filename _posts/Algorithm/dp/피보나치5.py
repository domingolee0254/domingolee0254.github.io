import sys

def main(n):
    fibo_list = [0, 1]
 
    for i in range(2, 21):
        
        if n == 0:
            return fibo_list[0]
        elif n == 1:
            return fibo_list[1]
        
        else:
           new = fibo_list[i-2] + fibo_list[i-1]
           fibo_list.append(new)
           if i == n:
               return fibo_list[i]
           else:
               pass
               
if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())

    ret = main(n)
    print(ret)
    
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b