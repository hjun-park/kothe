# 내 코드

# def solution(n):
#     answer = 0
#     while n > 0:
#         if n >= 500:
#             answer += n // 500
#             n %= 500
#         elif n >= 100:
#             answer += n // 100
#             n %= 100
#         elif n >= 50:
#             answer += n // 50
#             n %= 50
#         elif n >= 10:
#             answer += n // 10
#             n %= 10
#     print(answer)
#     return answer

# 효율적인 코드

def solution(n):
    count = 0

    coin_types = [500, 100, 50, 10]

    for i in coin_types:
        count += n // i
        n %= i
    return count

print(solution(1260))
