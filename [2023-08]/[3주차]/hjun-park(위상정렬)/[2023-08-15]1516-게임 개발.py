# 1516 - 게임 개발하기
import sys
from collections import deque

input = sys.stdin.readline

'''

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

10
20
14
18
17

N개 건물 지을 때 짓기 위해 필요한 최소 시간
N (건물 종류 수)
(1부터 N번까지)
T(건물시간), pre(사전필요건설건물), -1 (끝)

결과: 건물이 완성되기까지의 최소 시간 (N개)

'''
v = int(input().rstrip())
graph = [deque() for _ in range(v + 1)]
indegree = [0 for _ in range(v + 1)]
times = [0 for _ in range(v + 1)]


def topology():
    q = deque()
    time_result = [0 for _ in range(v + 1)]

    for node in range(1, v + 1):
        if indegree[node] == 0:
            q.append(node)

    while q:
        now = q.popleft()

        for nx in graph[now]:
            indegree[nx] -= 1
            time_result[nx] = max(time_result[nx], time_result[now] + times[now])
            if indegree[nx] == 0:
                q.append(nx)

    for i in range(1, v + 1):
        print(time_result[i] + times[i])


for n in range(1, v + 1):
    temp = list(map(int, input().split()))[:-1]
    times[n], pre_list = temp[0], temp[1:]

    for p in pre_list:
        graph[p].append(n)  # p -> n; n 건물이 지어지기 위해서는 p가 지어져야 한다.
        indegree[n] += 1    # n이 지어지기 위한 건물 수 증가 (indegree 증가)

topology()
