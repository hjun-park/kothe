from collections import deque
import sys

n = int(sys.stdin.readline())

que = deque(list(range(1, n + 1)))

while len(que) > 1:
    que.popleft()
    que.rotate(-1)

print(que[0])