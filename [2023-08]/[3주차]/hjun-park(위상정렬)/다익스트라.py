import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

'''
1) 필요정보
V(vertex), E(Edge)
start(시작지점)
graph(인접그래프)
visited(방문)
distance(최단거리)

2) 인접리스트 만들기
3) 최단거리 리스트 출발노드는 0, 나머지는 무한으로 초기화
--- for문 1번 ----
4) 최단거리 리스트에서 가장 값이 작은 노드 선택 (최초는 출발노트가 선택됨) (방문처리) (메서드로 만들기)
5) 4에서 선택된 노드에 연결된 값을 바탕으로 순회하면서 
    - 기존 있는 가중치와 들어온 가중치 비교하면서 업데이트
--- for문 2번 --- -> for문은 따로 한다.
6) 4-5 반복 
7) distance에 거리가 담기게 되고, distance가 INF라면 갈 수 없는 vertex 의미

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

0
2
3
7
INF
'''




# 노드의 개수, 간선 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
# a번 노드에서 b번 노드로 가는 비용이 c라는 의미
graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드 반환


def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]  # 노드까지의 거리

    # 시작 노드를 제외한 전체 n - 1
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])



import sys
import heapq
'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
input = sys.stdin.readline

# 필요한 변수 [입력]
# a) 노드의 개수 간선 [입력]
N, M = map(int, input().split())
# b) 시작 노드 번호 [입력]
start = int(input().rstrip())

# 필요한 변수 [고정]
# a) 그래프 [입력]
graph = [[] for i in range(N + 1)]
# b) INF = int(1e9)
INF = int(1e9)
# d) 최단거리 distance = [INF] * (n + 1)
distance = [INF] * (N + 1)

# step1. 모든 간선 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    # a -> b로 가는 비용이 c라는 의미
    graph[a].append([b, c])


# step2. 다익스트라 루프
def dijkstra(start):
    q = []

    # 1) 출발노드를 설정하고 큐에 넣기
    heapq.heappush(q, (0, start))   # (최단거리, 좌표)
    distance[start] = 0

    while q:
        # 2) 거리가 가장 짧은 노드를 꺼내서 확인
        dist, now = heapq.heappop(q)    # 거리, 현재위치

        # 3-1) 이미 짧은 거리로 갱신이 된 상태라면 갱신할 필요가 없음
        if distance[now] < dist:
            continue

        # 4) 갱신이 필요하다면 현재위치와 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]  # 이전 거리 + 현재 노드까지의 거리

            if cost < distance[i[0]]:    # 기존 경로보다 더 짧다면
                distance[i[0]] = cost   # 거리 갱신
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# step3. 모든 노드로 가기 위한 최단 거리 출력
#   - 도달할 수 없는 경우에는 INFINITY라고 출력
#   - 도달할 수 있는 경우에는 거리 출력
for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
