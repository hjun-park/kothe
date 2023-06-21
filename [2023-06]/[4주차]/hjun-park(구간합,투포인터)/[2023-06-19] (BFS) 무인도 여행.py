'''
 X : 바다
 1-9 : 무인도

 무인도는 상하좌우로 이어져있으면 하나의 무인도
 무인도 내 각 적혀진 숫자는 식량
 다 합하면 해당 무인도에서 최대 몇 일 머물 수 있는지 나타냄

 -> 각 섬에서 며칠 머물 수 있는지 오름차순 정렬 return

 0, visited 선언
 1. for문 돌면서 X가 아닌 숫자값을 찾음
 2. 숫자 값을 찾았다면 해당 값에 대해 BFS 순환,
  - 누적해서 bfs 탈출 시에 answer 배열에 담음,
 3. visited 체크하면서 계속해서 bfs 순환

'''

from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]

    def bfs(start_x, start_y):
        q = deque()
        q.append((start_x, start_y))
        visited[start_x][start_y] = True
        cnt = 0

        while q:
            x, y = q.popleft()
            cnt += int(maps[x][y])

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        q.append((nx, ny))
                        visited[nx][ny] = True

        return cnt

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))

    return sorted(answer) if answer else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 1, 27]
print(solution(["XXX", "XXX", "XXX"]))  # [-1]
