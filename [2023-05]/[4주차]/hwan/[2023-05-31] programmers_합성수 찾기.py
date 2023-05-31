def solution(n):
    answer = 0
    cnt = []
    for i in range(1, n+1):
        for j in range(1, i + 1):
            if i % j == 0:
                cnt.append(i)
    for i in set(cnt):
        if cnt.count(i) >= 3:
            answer += 1


    return answer

solution(15)