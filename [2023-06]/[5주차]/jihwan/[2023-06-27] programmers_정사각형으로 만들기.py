def solution(arr):
    answer = [[]]
    for i in range(len(arr)):
        if len(arr[i]) < len(arr):
            arr[i].extend([0] * (len(arr)-len(arr[i])))
    if len(arr[0]) > len(arr):
        for i in range(len(arr[0]) - len(arr)):
            arr.append([0] * len(arr[0]))

    answer = arr
    return answer