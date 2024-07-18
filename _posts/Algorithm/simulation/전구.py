import sys

def main(N, M, s, bulbs):
    for bulb in bulbs:
        a = bulb[0]
        b = bulb[1]
        c = bulb[2]
        
        if a == 1:
            s[b] = c
        elif a == 2:
            for i in range(b, c+1):
                if s[i] == 1:
                    s[i] = 0
                else:
                    s[i] = 1
        elif a == 3:
            s[b:c+1] = [0]*len(s[b:c+1])
        else:
            s[b:c+1] = [1]*len(s[b:c+1])
            
    return s[1:]

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    s = [0]+list(map(int, input().strip().split()))
    bulbs = [list(map(int, input().strip().split())) for _ in range(M)]
    ret = main(N, M, s, bulbs)
    print(" ".join(map(str, ret)))
    
#########################################################################
# sol 1
#########################################################################

# def main(N, M, s, bulbs):
#     for bulb in bulbs:
#         a, b, c = bulb
        
#         if a == 1:
#             s[b] = c
#         elif a == 2:
#             for i in range(b, c+1):
#                 s[i] = 1 - s[i]
#         elif a == 3:
#             for i in range(b, c+1):
#                 s[i] = 0
#         elif a == 4:
#             for i in range(b, c+1):
#                 s[i] = 1

#     return s[1:]