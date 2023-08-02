# 1707

'''

T (테스트케이스)
N, M (노드, 엣지)
graph (인접 그래프)
checked (이분 그룹)

1. 인접리스트 생성
2. 모든 노드에 대해서 BFS 순환 --> 순환 후 결과가 False가 나오면 NO, 루프빠져나오면 YES
3. BFS 로직

3-1. 기본 작업 후 while 시작
3-2. pop 이후 graph[i] 순회 시작
3-3. [방문하지 않았다면] 방문처리 후 그룹핑 처리 (+1 하고 2로  %계산)
3-4. [방문 했다면 그룹핑 같은지 체크]
    3-4-1. 같다면 return False
loop 그대로 나왔다면 return True


def bfs(start):
    q 초기화
    visited 초기화
    q.append(start)
    visited[start] = True
    checked 초기화 0

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                checked[i] = (checked[v] + 1) % 2
            elif checked[i] == checked[v]:
                return False

for i -> T:
    인접리스트 생성 (N+1)

    for i -> M:
        a, b <- input
        인접리스트 요소 이어주기(양방향)


    for i -> (1, N+1):
        is_bst = bfs(i)

        if not is_bst:
            print("NO")
            break
        else:
            continue

    print("YES")


2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

YES
NO

'''

import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = (visited[v] + 1) % 2
            elif visited[i] == visited[v]:
                return False
    return True


for _ in range(T):
    N, M = map(int, input().split())
    graph = [deque() for _ in range(N + 1)]
    visited = [-1] * (N + 1)
    is_bst = True

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        if visited[i] == -1:
            is_bst = bfs(i)
            if not is_bst:
                break

    print("YES" if is_bst else "NO")
