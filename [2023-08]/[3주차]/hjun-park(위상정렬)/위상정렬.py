import sys
from collections import deque

input = sys.stdin.readline

'''
[input]
5 6
1 2
1 3
2 4
2 5
3 4
4 5

[result]
1 2 3 4 5
'''

def topology():
    result = []
    q = deque()
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        # q에 들어간 것들은 차수가 0인 것들이기 때문에 결과에 담기
        result.append(node)
        for e in graph[node]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)

    for i in result:
        print(i, end=' ')


# DAG
V, E = map(int, input().split())
graph = [deque() for _ in range(V + 1)]
indegree = [0] * (V + 1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology()
