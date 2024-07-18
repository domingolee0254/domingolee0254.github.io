import sys

def main(N: int, M: int) -> None:
    # 매트릭스 초기화
    matrix = [[0] * N for _ in range(N)]
    
    # 방향 설정: 상, 우, 하, 좌
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction = 0  # 상 방향부터 이동
    y, x = N // 2, N // 2  # 정중앙 위치 초기화
    current_num = 1  # 그려줄 숫자
    matrix[y][x] = current_num
    
    # 타겟 숫자가 중앙인 경우 바로 위치 저장
    if current_num == M:
        tgt_pos = (y, x)
    
    length = 1  # 초기 이동 길이

    while current_num < N * N:
        for _ in range(2):  # 같은 길이로 두 번 이동
            for _ in range(length):
                if current_num >= N * N:
                    break
                next_x = x + directions[current_direction][1]
                next_y = y + directions[current_direction][0]

                if 0 <= next_x < N and 0 <= next_y < N and matrix[next_y][next_x] == 0:
                    x, y = next_x, next_y
                    current_num += 1
                    matrix[y][x] = current_num
                    if current_num == M:
                        tgt_pos = (y, x)
            
            current_direction = (current_direction + 1) % 4
        
        length += 1

    # 매트릭스 출력
    for row in matrix:
        print(" ".join(map(str, row)))
    
    # 타겟 넘버 출력
    print(tgt_pos[0] + 1, tgt_pos[1] + 1)  # 출력 형식에 맞는 인덱스로

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    M = int(input().strip())
    main(N, M)
