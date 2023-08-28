'''
0. v+1 만큼 빈 graph 생성, 거리 distance 생성 후 모두 INF 초기화
1. 값 입력받아 인접리스트 생성
2. start 지점만 거리 0으로 설정
3. 다익스트라 시작
 3-1. 최초 hq에 담음 (거리, 노드)
 3-2. while hq 시작
    1) 거리와 노드를 꺼냄
    2) 꺼낸 거리가 distance 보다 더 짧다면 이미 갱신된 것이므로 return
    3) 그게 아니라면 graph[node] 순회 시작
      i) cost는 현재 꺼낸 거리 + 이전 노드 거리
      ii) 만약 cost가 기존 노드보다 짧다면 distance 갱신 후 heapq에 넣어준다.
        ==> 넣어주는 이유는 거리가 짧으니까
'''
import heapq

N = int(input().rstrip())  # vertex
M = int(input().rstrip())  # edge

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())


def dijkstra():
    hq = []

    distance[start] = 0
    heapq.heappush(hq, [0, start])

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
            continue

        # [node, distance]
        for nxt in graph[now]:
            cost = dist + nxt[1]

            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(hq, [cost, nxt[0]])


dijkstra()

print(distance[end])
