def solution(arr):
    answer = []
    lst = [i for i, value in enumerate(arr) if value == 2]

    if len(lst) == 0:
        answer.append(-1)
    elif len(lst) == 1:
        answer.append(2)
    else:
        answer = arr[min(lst): max(lst) + 1]

    return answer


solution([1, 2, 1, 4, 5, 2, 9])
