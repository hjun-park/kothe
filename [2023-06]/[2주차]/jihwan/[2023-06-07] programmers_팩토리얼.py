def solution(n):
    answer = 0
    cnt = 1

    for i in range(1, n + 1):
        cnt *= i
        if cnt <= n:
            answer = i
        else:
            break


    return answer


solution(3628800)