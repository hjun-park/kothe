def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])

        else:
            if answer[-1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    return answer