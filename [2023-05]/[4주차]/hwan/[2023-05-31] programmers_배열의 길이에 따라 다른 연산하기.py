def solution(arr, n):
    answer = []

    for i in range(len(arr)):
        if len(arr) % 2 != 0:
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
        else:
            if i % 2 != 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])

    return answer

solution([49, 12, 100, 276, 33], 27)