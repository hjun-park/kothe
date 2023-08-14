# 2252 - 줄 세우기
import sys
from collections import deque

input = sys.stdin.readline

'''
- 정렬 해야 할 것 같은데 가중치 주고 매번 정렬하기엔 시간복잡도 오류 날 것 같고
 --> 이럴 때 topology sort 사용
3 2
1 3
2 3

1 2 3

4 2
4 2
3 1

3 4 1 2
'''

v, e = map(int, input().split())
graph = [deque() for _ in range(v + 1)]
indegree = [0 for _ in range(v + 1)]


def topology():
    q = deque()
    topology_rst = []

    for n in range(1, v + 1):
        if indegree[n] == 0:
            q.append(n)

    while q:
        node = q.popleft()
        topology_rst.append(node)

        for n in graph[node]:
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)

    for r in topology_rst:
        print(r, end=' ')


for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology()
