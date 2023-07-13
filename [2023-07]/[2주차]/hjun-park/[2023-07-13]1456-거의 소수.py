# 핵심: 에라토스테네스의 체를 이용해서 B까지 전부 순회하는 것이 아닌 제곱근까지만 순회해야 한다.
import sys
from math import sqrt

input = sys.stdin.readline

A, B = map(int, input().split())

arr = [x for x in range(0, int(sqrt(B))+1)]
arr[1] = 0

for i in range(2, int(sqrt(B)) + 1):
    if arr[i] == 0:
        continue
    # 관련 배수는 모두 소수가 아님 (에라토스테네스의 체)
    for j in range(i+i, int(sqrt(B))+1, i):
        arr[j] = 0

cnt = 0

for i in range(2, int(sqrt(B)) + 1):
    if arr[i] == 0:
        continue
    mul = arr[i]
    while arr[i] <= B / mul:
        if A / mul <= arr[i]:
            cnt += 1
        mul *= arr[i]

print(cnt)


# def solution(A, B):
# print(solution(1, 1000))    # 25
# print(solution(1, 10))    # 3
# print(solution(5324, 894739))   # 183
