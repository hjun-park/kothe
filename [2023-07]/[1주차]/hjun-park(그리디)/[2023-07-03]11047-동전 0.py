import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(N)]

cnt = 0
for coin in coins[::-1]:
    if coin <= K:
        q, r = divmod(K, coin)
        cnt += q
        K = r

print(cnt)
