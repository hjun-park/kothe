def solution(num_list):
    answer = 0

    for i in num_list:
        while i > 1:
            answer += 1
            if i % 2 == 0:
                i /= 2
            else:
                i = (i - 1) / 2

    return answer

solution([12, 4, 15, 1, 14])