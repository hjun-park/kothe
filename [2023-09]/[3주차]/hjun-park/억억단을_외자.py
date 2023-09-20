'''
- 핵심 : 숫자의 등장 횟수는 해당 수의 약수와 동일

1) starts 중 가장 작은 것부터 시작해서 e까지 약수 개수를 구한다.
2) 메모이제이션을 이용해서 가장 많이 등장하는 수를 찾는다.

'''


def solution(e, starts):
    # 1. 약수의 개수를 저장할 리스트 선언 (인덱스: 숫자, 값: 약수 갯수)
    divisors = [0] * (e + 1)
    # 2. 시작점 선언
    min_start = min(starts)

    # === 약수 개수 구하는 과정 === #
    # 3. 메모이제이션 이용
    for i in range(1, e + 1):
        # 1. 제곱수에 대해서는 약수의 개수 1 증가
        if i * i <= e:
            divisors[i * i] += 1
        # 2. start부터 end까지 수행
        for j in range(i + 1, e + 1):
            # 1. 두 수를 곱한 결과는 그 결과의 약수이기도 함
            n = i * j
            # 2. 범위를 벗어난 경우 논외
            if n > e:
                break
            # 3. 두 수 i, j 모두 n의 약수이기 때문에 2를 더함
            divisors[n] += 2

    # === 최대 약수 구하는 과정 === #
    # 4. 각 숫자에 대해 최대 약수를 구할 리스트 정의
    max_divisors = [0] * (e + 1)

    # 4-.모든 숫자의 최대 약수가 e로 되게끔
    max_divisors[-1] = e

    # 5. 이번엔 역순으로 순회
    for i in range(e - 1, min_start - 1, -1):
        # 1. divisors[i] : 현재 위치의 약수 개수
        # 2. 다음 약수 개수 <= 현재 약수 개수
        if divisors[max_divisors[i + 1]] <= divisors[i]:
            # 1. 현재 위치 약수 개수가 더 많은 경우
            max_divisors[i] = i
        else:
            # 2.이전 위치의 최대 약수 유지
            max_divisors[i] = max_divisors[i + 1]

    answer = [max_divisors[s] for s in starts]

    return answer
