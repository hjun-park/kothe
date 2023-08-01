# 1325

'''
N(노드)
M(엣지)
graph(인접 리스트) - (N+1)
answer(노드 당 신뢰관계 개수 0 초기화) - (N+1)

for 엣지순회:
    a, b <- 입력
    양방향 연관관계 생성

BFS(start):
    q 초기화
    q에 start 담음
    visited False로 초기화 (N+1)
    시작점 visited True 설정

    while q:
        v = q.popleft()
        v를 참고하는 여러 노드들을 추가적으로 순회 후 큐에 담음(방문하지 않아야함)

    visited(True)의 개수를 반환

1부터 i -> N+1까지 순회:
    cnt = bfs(i)
    answer[i] = cnt

_max = max(answer)

1부터 N+1까지 순회:
    if _max == answer[i]:
        print(i, end=' ')



5 4
3 1
3 2
4 3
5 3


1 2

'''

from collections import deque

N, M = map(int, input().split())
graph = [deque() for _ in range(N + 1)]
answer = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                q.append(i)


for i in range(1, N + 1):
    bfs(i)

_max = max(answer)

for i in range(1, N + 1):
    if _max == answer[i]:
        print(i, end=' ')
