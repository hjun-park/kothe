def solution(n):
    answer = []
    for i in range(n):
        lst = [0] * n
        lst[i] += 1
        answer.append(lst)
    return answer

solution(3)