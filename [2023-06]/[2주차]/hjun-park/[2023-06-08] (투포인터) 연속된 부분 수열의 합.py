'''
[투포인터]
- 매번 sum을 구하는 것이 아닌, 누적합을 구함
'''


def solution(sequence, k):
    answer = []

    # 1. 투포인터 지정
    left, right = 0, 0

    # 2. 현재 누적합을 첫 인덱스로 잡음
    current_sum = sequence[0]

    # 3. 투포인터 시작
    while right < len(sequence):
        # 1. 만약 현재 누적합이 k와 같다면 (left, right) 같이 움직임
        if current_sum == k:
            answer.append([left, right])    # 1. 두 인덱스를 정답에 추가
            current_sum -= sequence[left]   # 2. left 감소 전 누적합 감소
            left += 1                       # 3. left 이동
            right += 1                      # 4. right 이동
            if right < len(sequence):           # 5. right 이동했으니 인덱스 체크 후 누적합 증가
                current_sum += sequence[right]
        # 2. 만약 현재 누적합이 k보다 작다면 (right)만 움직여서 누적합 키우기
        elif current_sum < k:
            right += 1                          # 1. 더 큰 수를 더하기 위해 right 이동
            if right < len(sequence):           # 2. right 이동했으니 인덱스 체크 후 누적합 증가
                current_sum += sequence[right]
        # 3. 만약 현재 누적합이 k보다 크다면 (left)만 움직여서 누적합 줄이기
        else:
            current_sum -= sequence[left]       # 1. right와는 반대로 먼저 뺀 후에 left 이동
            left += 1

    # 4. 배열 사이즈가 가장 작은 것 먼저, 그 다음으로 인덱스가 빠른 순서대로 정렬
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]


print(solution([1, 2, 3, 4, 5], 7))  # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # [6, 6]
print(solution([2, 2, 2, 2, 2], 6))  # [0, 2]
