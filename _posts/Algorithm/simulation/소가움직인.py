import sys

def main(N:int, obs_list:list) -> int:
    
    mv_list = [-1]*11
    mv_cnt = 0

    for obs in obs_list:
        cow_idx, cow_loc = obs[0], obs[1]
        # 처음 관측된 위치
        if mv_list[cow_idx] == -1:
            mv_list[cow_idx] = cow_loc
        
        # 처음이 아닐 경우
        else:
            # 같은 위치일 경우
            if mv_list[cow_idx] == cow_loc:
                pass
            # 위치를 이동한 경우
            else:
                mv_list[cow_idx] = cow_loc
                mv_cnt += 1

    return mv_cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    obs_list = [list(map(int, input().strip().split())) for _ in range(N)]
    ret = main(N, obs_list)
    print(ret)