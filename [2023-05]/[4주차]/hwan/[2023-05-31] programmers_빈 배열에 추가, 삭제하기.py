def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            answer.extend([arr[i]]*(arr[i]*2))
        else:
            answer = answer[0:len(answer) - arr[i]]

    return answer

solution([3, 2, 4, 1, 3], [True, False, True, False, False])