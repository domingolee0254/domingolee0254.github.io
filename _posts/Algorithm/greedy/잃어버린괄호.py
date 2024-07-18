# 1. 입력 문자열을 '-' 기준으로 분리
# 2. 분리된 각 부분을 '+' 기준으로 다시 분리하여 숫자들을 합
# 3. 첫 번째 부분은 더한 결과를 시작 값으로 하고, 이후 부분들은 빼는 방식으로 결과를 계산
import sys

def minimize_expression(expression):
    body = 0
    parts = expression.split('-')
    
    head = sum(map(int, parts[0].split('+')))
    
    for part in parts[1:]:
        body += sum(map(int, part.split('+')))
#         total -= sum(map(int, part.split('+')))

    total = head - body
    
    return total

if __name__ == "__main__":
    input = sys.stdin.readline
    expression = input().strip()
    ret = minimize_expression(expression)
    print(ret)