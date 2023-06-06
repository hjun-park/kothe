# Greedy + Sliding window ?
'''
    핵심은 1사분면만 점의 개수를 구하고 *4 를 구한다.
    x축, y축 둘 다 구하면 중복이 발생하는 것에 주의

    피타고라스 정리를 이용 c^2 = a^2 + b^2
     -> 1사분면 기준으로 x가 증가함에 따라 원의 반지름 r은 그대로인 반면, y는 감소하는 형태
'''


def solution(r1, r2):
    count = 0

    # 1. 두 원의 최대 높이는 각 원의 반지름
    y_min, y_max = r1, r2

    # 2. x는 가장 큰 원의 반지름까지 움직임
    for x in range(0, r2):
        # 1. 원 반지름 내에 들 수 있도록 y_max 지정
        # 문제의 초록색 1사분면처럼 x가 증가함에 따라 y_max는 감소함
        while x ** 2 + y_max ** 2 > r2 ** 2:
            y_max -= 1

        # 2. 원 반지름 내에 들 수 있도록 y_min 지정
        #   중복으로 세는 것을 방지하기 위해 x는 0부터 시작하지만 y는 1부터 시작함
        #   문제의 파란색 1사분면처럼 x가 증가함에 따라 y_min은 감소함
        while y_min > 1 and x ** 2 + (y_min - 1) ** 2 >= r1 ** 2:
            y_min -= 1

        # 1을 더한 이유는 1 ~ 3 사이의 수 갯수를 구하기 위해 3-1+1 하는 것과 같다.
        count += (y_max - y_min + 1)

    return count * 4


print(solution(2, 3))  # 20
