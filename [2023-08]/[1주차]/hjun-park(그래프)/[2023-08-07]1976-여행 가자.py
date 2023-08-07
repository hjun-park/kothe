# 1976 - 여행 계획 짜기
'''
3
3
0 1 0
1 0 1
0 1 0
1 2 3

YES

1. 도시N개
2. M개 계획 (M개의 연결된 도시정보)
3. 1이면 연결(양방향)되고, 0이면 연결되지 않음
4. 도시번호는 1번부터



# cycle detection in graph (union-find 이용)
1. 서로소 집합을 만든다 ( 자기가 자기 자신을 가리키는 노드들 )
2. 입력받은 수에 대해 union을 만든다.
3. 마지막 입력받은 수 들이 모두 같은 부모인지 확인한다.


----------------------------
주의점 : 도시는 0이 아닌 1부터 시작하기 때문에 2차원 배열은 [1][1]부터 시작해야 한다.
즉, [0][X], [X][0]에 zero-padding을 넣어야 하는데, 아래와 같이 해결한다.

[기존] - zero padding 넣기 곤란
graph = [list(map(int, input().split())) for _ in range(N)]

[권장] - 미리 만들고 매 입력마다 zero-padding을 넣는다.
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
   graph[i] = [0] + list(map(int, input().split()))

-----------------------------

'''


import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

parent = [-1] * (N+1)
# graph = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * (N+1) for _ in range(N+1)]


# 코드에 대한 상세한 설명은 1717번 참고
def find(x):
   if parent[x] < 0:
      return x

   parent[x] = find(parent[x])
   return parent[x]


def union(a, b):
   a = find(a)
   b = find(b)

   if a == b:
      return

   # union
   if parent[a] < parent[b]:   # a의 높이가 더 큼
      parent[a] += parent[b]
      parent[b] = a
   else:
      parent[b] += parent[a]
      parent[a] = b



for i in range(1, N+1):
   graph[i] = [0] + list(map(int, input().split()))

cities = list(map(int, input().split()))

for i in range(1, N+1):
   for j in range(1, N+1):
      if graph[i][j] == 1:
         union(i, j)


p = find(cities[0])
for city in cities[1:]:
   if p != find(city):
      print("NO")
      break
else:
   print("YES")
