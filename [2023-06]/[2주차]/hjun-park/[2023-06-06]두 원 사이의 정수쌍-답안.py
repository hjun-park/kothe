from math import sqrt


def solution(r1, r2):
    cnt = 0
    # 맨 처음
    for x in range(0, r1):
        cnt += int(sqrt(r2 ** 2 - x ** 2)) - int(sqrt(r1 ** 2 - x ** 2 - 1))
    # 작은 원의 높이가 0이 되는 순간
    for x in range(r1, r2):
        cnt += int(sqrt(r2 ** 2 - x ** 2))
    return cnt * 4


print(solution(2, 3))  # 20
