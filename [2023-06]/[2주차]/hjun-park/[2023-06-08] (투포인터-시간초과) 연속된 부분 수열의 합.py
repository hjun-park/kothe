'''
[투포인터]
- 시간초과 이유 : 매번 sum을 이용해서 구함
'''


def solution(sequence, k):
    answer = []
    left, right = 0, 1

    while right <= len(sequence):
        num = sum(sequence[left:right])

        if num == k:
            answer.append([left, right - 1])
            left += 1
            right += 1
        elif num > k:
            left += 1
        else:
            right += 1

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]


print(solution([1, 2, 3, 4, 5], 7))  # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # [6, 6]
print(solution([2, 2, 2, 2, 2], 6))  # [0, 2]
