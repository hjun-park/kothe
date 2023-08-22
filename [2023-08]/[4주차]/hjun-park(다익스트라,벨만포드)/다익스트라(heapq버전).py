import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input().rstrip())

INF = int(1e9)
graph = [[] for _ in range(v + 1)]
distance = [INF for _ in range(v + 1)]

# 1. 인접리스트 생성
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


# 2. 다익스트라 시작
def dijkstra(start):
    hq = []

    # 1. hq에 담음 (거리, 노드)
    heapq.heappush(hq, [0, start])
    distance[start] = 0

    # 2. while hq
    while hq:
        dist, node = heapq.heappop(hq)
        # 1. 노드를 꺼낸 후 이미 짧은 거리로 갱신되어 있다면 continue (기존 다익스트라 버전의 visited 처리)
        if distance[node] < dist:
            continue

        # 2. 아니라면 그 다음 노드들을 순회하면서 이전 거리 + 현재 노드까지 거리 계산 후
        for i in graph[node]:
            cost = dist + i[1]  # 이전 거리 + 현재 노드까지 거리

            # 3. 기존 경로보다 더 짧은 경우엔
            if cost < distance[i[0]]:
                # 1. distance 갱신
                distance[i[0]] = cost
                # 2. heapq에 넣어준다.
                heapq.heappush(hq, [cost, i[0]])



# 3. 순회하며 출력
dijkstra(start)

# step3. 모든 노드로 가기 위한 최단 거리 출력
#   - 도달할 수 없는 경우에는 INFINITY라고 출력
#   - 도달할 수 있는 경우에는 거리 출력
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
