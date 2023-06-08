def solution(n):
    answer = []
    num = 2
    while n > 1:
        if n % num == 0:
            n /= num
            answer.append(num)
        else:
            num += 1
    return sorted(list(set(answer)))

solution(12)