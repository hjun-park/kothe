def solution(n):
    answer = []
    answer.append(n)
    while n != 1:
        if n % 2 ==0:
            n /= 2
            answer.append(int(n))
        else:
            n = n * 3 + 1
            answer.append(int(n))
    return answer

solution(10)