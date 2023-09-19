def solution(k, score):
    answer = []
    lst = []
    for i in score:
        lst.append(i)
        lst.sort()
        if len(lst) < k:
            answer.append(lst[0])
        else:
            answer.append(lst[-k])
    return answer

solution(3, [10, 100, 20, 150, 1, 100, 200])
