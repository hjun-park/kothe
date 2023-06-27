def solution(arr):
    answer = []
    n = 0
    for i in range(len(arr)):
        if len(arr) <= 2 ** i:
            n = i
            arr.extend([0] * (2 ** n - len(arr)))
            break

    answer = arr

    return answer