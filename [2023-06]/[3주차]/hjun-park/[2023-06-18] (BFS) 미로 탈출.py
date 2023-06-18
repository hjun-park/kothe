from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def solution(maps):
    N, M = len(maps), len(maps[0])
    start = end = lever = ''

    def bfs(sx, sy, ex, ey):
        q = deque()
        q.append((sx, sy))
        visited = [[-1] * M for _ in range(N)]
        visited[sx][sy] = 0

        while q:
            x, y = q.popleft()

            if x == ex and y == ey:
                return visited[x][y]

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny] == -1 and maps[nx][ny] != 'X':
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

        return -1

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    answer = 0
    temp = bfs(start[0], start[1], lever[0], lever[1])
    if temp == -1:
        return -1
    else:
        answer += temp

    temp = bfs(lever[0], lever[1], end[0], end[1])
    if temp == -1:
        return -1
    else:
        answer += temp

    return answer


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
