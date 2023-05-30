def solution(num_list, n):
    answer = []
    lst = num_list[n::]
    answer = lst + num_list[:n]
    return answer

solution([5, 2, 1, 7, 5], 3)