import sys

def main(diary):
    # 유제품의 가격을 내림차순으로 정렬 - 비싼 제품을 빼는 게 좋은 전략이니까
    diary.sort(reverse=True)
    total_cost = sum(diary)

    # 3번째마다 있는 유제품의 가격을 총합에서 뺌
    # 인덱스는 0부터 시작하므로, 2, 5, 8,...이 3번째마다의 유제품임
    for i in range(2, len(diary), 3):
        total_cost -= diary[i]  # 3번째 유제품의 가격을 뺌
    
    return total_cost


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    diary = [int(input().strip()) for _ in range(N)]
    ret = main(diary)
    print(ret)
