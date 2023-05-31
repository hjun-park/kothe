def solution(arr):
    answer = 0
    lst = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                lst.append(1)
            else:
                lst.append(0)
    if 0 in lst:
        answer = 0
    else:
        answer = 1
    return answer

solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]])