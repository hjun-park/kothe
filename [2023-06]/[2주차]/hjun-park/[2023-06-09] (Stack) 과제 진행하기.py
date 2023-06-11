'''
    [Stack]
'''


def solution(plans):
    answer = []
    left = []

    # 1. 시작 시간 순으로 정렬
    plans.sort(key=lambda x: x[1])

    for next_name, next_start, next_playtime in plans:
        # 1. 시간 파싱 후 분 단위로 변환
        h, m = map(int, next_start.split(':'))
        next_start = h * 60 + m
        next_playtime = int(next_playtime)

        # 2. 다 하지 못한 과목이 있다면
        if left:

            # 1. 이전 내용을 가져옴
            name, start, playtime = left.pop()

            # 2. 다음 과제 시작 시간 - 현재 과제 시작 시간
            #  -> 가용할 수 있는 과제 시간을 구함
            extra_time = next_start - start

            # 3. 가용 가용한 시간 내로 과제 수행이 불가능한 경우
            if extra_time < playtime:
                # 1. 일단 가용 가능한 시간은 과제 수행 하고 나머지는 left에 집어 넣는다.
                left.append((name, start, playtime - extra_time))
            # 4. 가용 가능한 시간 내로 과제 수행이 가능한 경우
            else:
                # 1. 과제를 끝냈으니 과제 이름을 결과에 담는다.
                answer.append(name)

                # 2. 과제를 수행하고 남은 시간을 구한다.
                extra_time = extra_time - playtime

                # 3. 해야 할 과제가 있고 남은 시간도 있다면
                while left and extra_time:
                    # 1. 남은 과제에서 가져온다.
                    name, start, playtime = left.pop()

                    # 2. 만약 남은 시간 내로 과제 수행을 할 수 없다면
                    if extra_time < playtime:
                        # 1. 일단 할 만큼 과제를 하고 다시 `left`에 집어 넣는다.
                        left.append((name, start, playtime - extra_time))
                        # 2. 남은 시간만큼 과제 수행 했으니 loop 빠져 나온다/
                        break
                    # 3. 시간 내로 과제 수행이 가능하면
                    else:
                        # 1. 수행하였으니 과제 이름을 결과에 담는다.
                        answer.append(name)
                        # 2. 과제를 수행하고 남은 시간을 구한다. 남은 시간이 없을 때까지 다음 루프를 수행한다.
                        extra_time = extra_time - playtime

        # 3. 일단 `left`에 넣고봄
        left.append((next_name, next_start, next_playtime))

    answer.extend([s for s, _, _ in left[::-1]])

    return answer


# ['과제이름' '시작시간', '소요시간(분)']
# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution(
    [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
