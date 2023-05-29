def solution(ss):
    answer = 0
    x_cnt = 0
    remain_cnt = 0
    for s in ss:
        if x_cnt == remain_cnt:
            answer += 1
            x = s

        if s == x:
            x_cnt += 1
        else:
            remain_cnt += 1
    return answer
