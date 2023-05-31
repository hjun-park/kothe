def solution(arr):
    answer = []
    for i in arr:
        answer.extend([i] * i)

    return answer

solution([5, 1, 4])