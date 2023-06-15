'''


'''

from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def solution(board):
    # cnt = 0  # 미끄러져 이동하는게 한 번

    q = deque()
    visited = set()

    def bfs():
        while q:
            x, y, cnt = q.popleft()

            if board[x][y] == 'G':
                return cnt

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                # 11, 13, 15번 케이스 런타임 에러
                # # rx, ry = x, y가 while 안에만 있다면 이동할 수 없을 때 rx, ry에 값을 못 담으므로
                # # while 바깥에도 rx, ry 선언
                rx, ry = x, y
                while (0 <= nx < len(board)) and (0 <= ny < len(board[0])) and board[nx][ny] != 'D':
                    rx, ry = nx, ny
                    nx += dx[d]
                    ny += dy[d]

                if (rx, ry) not in visited:
                    visited.add((rx, ry))
                    q.append((rx, ry, cnt + 1))

        return -1

    # 1. 보드를 순회하면서 값을 찾음
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                break

    answer = bfs()

    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
print(solution(["RG."]))
