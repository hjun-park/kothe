def solution(arr):
    stk = []
    cnt = 0
    while cnt < len(arr):
        if len(stk) == 0:
            stk.append(arr[cnt])
            cnt += 1
        elif stk[-1] < arr[cnt]:
            stk.append(arr[cnt])
            cnt += 1
        elif stk[-1] >= arr[cnt]:
            stk.pop()

    return stk

solution([1,4,2,5,3])