def solution(num_list):
    answer = 1
    if len(num_list) < 11:
        for i in num_list:
            answer *= i
    else:
        answer = sum(num_list)
    return answer
solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1])