def solution(k, m, score):
    answer = 0
    lst = []
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        lst.append(score[i: i + m])

    for i in lst:
        if len(i) == m:
            answer += (min(i) * m)

    return answer


solution(3, 4, [1, 2, 3, 1, 2, 3, 1])
