import sys

input = sys.stdin.readline

v, e = map(int, input().split())
INF = int(1e9)
start = 1
edges = []
distance = [INF for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

distance[start] = 0

for _ in range(v-1):
    for edge in edges:
       start, end, cost = edge

       # 현재 간선을 거쳐서 가는 것이 더 빠른 경우 갱신
       if distance[start] != INF and distance[end] > distance[start] + cost:
          distance[end] = distance[start] + cost

isCycle = False
for edge in edges:
   start, end, cost = edge

   if distance[start] != INF and distance[end] > distance[start] + cost:
      isCycle = True
      break


if not isCycle:
   for i in range(2, v+1):
      if distance[i] != INF:
         print(distance[i])
      else:
         print(-1)
else:
   print(-1)

