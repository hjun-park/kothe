#  내 코드
# 시간초과 에러가 나서 컴프리헨션을 사용했지만 그래도 시간초과 에러가 남

# def solution(number, limit, power):
#     answer = 0
#
#     lst = [list((x for x in range(1, i + 1) if i % x == 0)) for i in range(1, number + 1)]
#
#     for i in lst:
#         if len(i) > limit:
#             answer += power
#         else:
#             answer += len(i)
#     return answer

# 답은 보지 않았지만 효율적으로 약수 구하는 코드 참고

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:  # 나눠지면 더하기 2, i 의 약수는 j 와 i//j 두 개씩 존재하기에
                cnt += 2
                if j ** 2 == i: # 제곱근과 겹치면 1 빼줌
                   cnt -= 1
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer


solution(5, 3, 2)
