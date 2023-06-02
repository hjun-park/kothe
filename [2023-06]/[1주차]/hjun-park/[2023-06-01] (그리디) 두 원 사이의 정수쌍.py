'''
 1) r1이상 r2미만 수들을 구한다.
 2) 해당 수들을 순회 하면서 answer 구한다.
 3) 4 + (4 * ( 2^i ))
  -> 처음 4 : 바깥 원  정수
'''


def solution(r1, r2):
    answer = 0

    for i in range(r1, r2):
        answer += (4 + (4 * 2 ** i))

    return answer


# print(solution(2, 3))  # 20
# print(solution(1, 2))  # 12
print(solution(1, 1_000_000))
