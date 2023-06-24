def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
    if len(answer) >= k:
        answer = answer[:k]
    else:
        answer.extend([-1] * (k - len(answer)))

    return answer