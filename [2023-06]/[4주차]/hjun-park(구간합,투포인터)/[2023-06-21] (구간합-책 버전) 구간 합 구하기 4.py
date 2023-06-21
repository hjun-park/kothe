import sys

input = sys.stdin.readline

'''
numbers 변수에 숫자 데이터 저장
prefix_sum 합 배열 변수 선언
temp 누적 합을 담을 변수

for 숫자 순대로 탐색:
    temp에 숫자 더해서 누적합 만들기
    prefix_sum 합 배열에 temp 저장
    
for 문제 인자 구하기:
    범위 a, b 입력 받기
    a, b 구간합 출력
'''

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]  # 누적합 구하기 쉽게 초기에 0을 담음
temp = 0

for n in nums:
    temp += n
    prefix_sum.append(temp)

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])

'''
5 3
5 4 3 2 1
1 3
2 4
5 5
'''
