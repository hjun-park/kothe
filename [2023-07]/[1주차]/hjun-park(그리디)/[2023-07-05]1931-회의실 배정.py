import sys

input = sys.stdin.readline

N = int(input().rstrip())
times = [list(map(int, input().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))

cnt = 0
before_end = -1
for start, end in times:
    if before_end <= start:
        cnt += 1
        before_end = end

print(cnt)
