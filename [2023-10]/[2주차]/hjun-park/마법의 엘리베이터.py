def solution(storey):
    answer = 0

    while storey:
        storey, r = divmod(storey, 10)

        # 0 - 4
        if r < 5:
            answer += r
            continue
        # 6 - 9
        elif r > 5:
            answer += (10-r)
            storey += 1

        # 5의 경우 다음 자릿수에 따라서 더할 지, 뺄 지 정해진다.
        # 55일 때 맨 뒷자리 5가 더하고 뺄 때 횟수가 얼만큼 차이나는지 확인하면 된다.
        # [더하는경우] 55 -> 60 -> 100 -> 0 ( 5 + 4 + 1 = 10 )
        # [빼는 경우] 55 -> 50 -> 100 -> 0 ( 5 + 5 + 1 = 11 )
        # https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EB%A7%88%EB%B2%95%EC%9D%98-%EC%97%98%EB%A6%AC%EB%B2%A0%EC%9D%B4%ED%84%B0-Python

        else:
            if storey % 10 >= 5:
                answer += (10-r)
                storey += 1
            else:
                answer += r

    return answer


assert solution(16) == 6
assert solution(2554) == 16
assert solution(1) == 1
assert solution(5) == 5
assert solution(8) == 3
assert solution(10) == 1
assert solution(99) == 2
assert solution(545) == 14
assert solution(646) == 13
assert solution(95) == 6
assert solution(5) == 5
