def solution(box, n):
    answer = 1
    lst = []
    for i in box:
        lst.append(int(i / n))
    for i in lst:
        answer *= i
    return answer

solution([10, 8, 6] , 3)