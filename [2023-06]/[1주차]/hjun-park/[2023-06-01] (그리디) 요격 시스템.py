'''
    핵심 :
        1) 좌표 e를 기준으로 target 정렬 후에
        2) [bs, be][s, e] 가 있다면, 이전 미사일이 끝나는 좌표인 be와 현재 미사일의 s를 비교
        3) 만약 s가 be보다 같거나 크다면 겹치지 않아서 요격할 수 없다.
'''


def solution(targets):
    answer = 0

    # 1. 미사일 끝 e를 기준으로 졍렬
    targets.sort(key=lambda x: (x[1], x[0]))

    # 2. 이전 미사일 처음과 끝 초기화
    s, e = 0, 0
    for ts, te in targets:
        # 1. 이전 미사일 끝(e) <= 현재 미사일 처음(ts)
        #  -> e와 ts가 같아도 요격할 수 없는 이유는 그림으로 봤을 때 연속된 값이라 겹칠 수 없음
        if e <= ts:
            answer += 1
            e = te

        # 2. 그렇지 않다면 e를 갱신하지 않음 ( e보다 더 큰 ts를 만날 때까지 미사일 추가 필요없음)

    return answer


print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))
