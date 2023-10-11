from collections import Counter

def solution(weights):
    answer = 0

    # 1. Counter를 통해서 1:1 비율인 애들을 셈
    # Counter 선언
    # Counter item 순환하면서 2개 이상인 경우는 vC2 만큼 answer에 반영
    counter = Counter(weights)

    for v in counter.values():
        if v >= 2:
            answer += (v * (v-1)) // 2

    # 2. 1:1은 세었으니, set을 이용해서 중복 제거
    weights = set(weights)

    # 3. 2:3, 2:4, 3:4 를 세어야 한다.
    # weights를 순회하면서 w * 2/3, 2/4, 3/4 곱해서 반영
    '''
        answer += 1 이 아닌 
        answer += counter[w * 2/3] * counter[w] 한 이유는
        중복된 요소가 여러 개 일 수 있어서이다. (w도 여러개, w * 2/3도 여러개 가능성)
        
        [120, 120, 80, 80, 80] 에서
        1:1 비율의 짝꿍은 -> 1 + 3 = 4개
        2:3, 2:4, 3:4 비율 짝꿍 -> counter[w * 2/3] * counter[w] = 3 * 2 = 6개
        
        총합 10개 
    
    '''
    # counter[k] = v   weights 에서 k 수를 가지는 요소 v개
    for w in weights:
        if w * 2/3 in weights:
            answer += counter[w * 2/3] * counter[w]
        if w * 2/4 in weights:
            answer += counter[w * 2/4] * counter[w]
        if w * 3/4 in weights:
            answer += counter[w * 3/4] * counter[w]

    return answer


# print(solution([100, 180, 360, 100, 270]))
# print(solution([120, 120, 80, 80, 80]))
# print(solution([100, 100, 100, 100, 100, 100]))
# print(solution([150, 180, 200, 220, 250]))
