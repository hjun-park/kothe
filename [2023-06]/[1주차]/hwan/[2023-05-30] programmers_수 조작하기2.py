def solution(numLog):
    answer = ''
    lst = []
    for i in range(1, len(numLog)):
        lst.append(numLog[i] - numLog[i - 1])

    for i in lst:
        if i == 1:
            answer += "w"
        elif i == -1:
            answer += "s"
        elif i == 10:
            answer += "d"
        elif i == -10:
            answer += "a"
    return answer