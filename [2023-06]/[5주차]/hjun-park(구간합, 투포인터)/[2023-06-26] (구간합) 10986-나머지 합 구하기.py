import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

D = [0] * N     # 누적합을 담을 배열
C = [0] * N     # 나머지의 인덱스를 카운트 C[1] 이라면 누적합 배열 D의 나머지 개수를 의미
D[0] = A[0]     # 누적합 시작

cnt = 0

# 누적합 계산
for i in range(1, N):
    D[i] = D[i - 1] + A[i]

for i in range(N):
    # 누적합을 M으로 나눠서 나머지를 구한다.
    D[i] %= M

    # 나머지가 0이라면 문제에서 요구하는 경우의 수
    if D[i] == 0:
        cnt += 1
    # 인덱스 증가
    C[D[i]] += 1

for i in range(M):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우 2C2
    if C[i] > 1:
        cnt += C[i] * (C[i] - 1) // 2

print(cnt)
