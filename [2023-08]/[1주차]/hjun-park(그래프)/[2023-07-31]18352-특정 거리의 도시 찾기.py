# 18352

import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [deque() for _ in range(N + 1)]
answer = []
visited = [-1 for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)


bfs(X)

for i in range(1, N + 1):
    if visited[i] == K:
        answer.append(i)

print(-1 if not answer else '\n'.join(map(str, answer)))
