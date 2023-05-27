def solution(n, m, section):
    answer = 0

    while section:
        start = section.pop(0)
        while section and section[0] < start + m:
            section.pop(0)

        answer += 1

    return answer


print(solution(8, 4, [2, 3, 6]))
# print(solution(5, 4, [1, 3]))
# print(solution(4, 1, [1, 2, 3, 4]))
# print(solution(100, 4, [2, 3, 99]))  # 2
# print(solution(1, 1, [1]))  # 1
