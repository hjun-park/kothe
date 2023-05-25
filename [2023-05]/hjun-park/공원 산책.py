'''

1. 강아지 특성
    - 다음 이동지역이 장애물 혹은 공원 밖 : 명령어 무시
    - 나머지 : 이동

2. keyword
    park : 공원그래프
        - S: 시작점
        - O: 이동가능
        - X: 이동 불가능
    routes : 강아지가 수행할 명령어
    [op n]  : 명령어 구조 (op: 이동방향 : n : 이동 칸)
        - N, S, W, E

3. 구하고자 하는 것
 - 최종 목적지 x, y 좌표
'''

'''
    단순구현
    1. 이동방향 N S W E 에 대해서 dictionary 만들기
    2. 시작점 좌표 찾기 (x, y)
    3. routes 명령어 순회 (파싱)
    4. 명령어 수행 후 위치 계산 (nx, ny)
    5. 계산된 위치가 공원을 벗어나거나 장애물이 있는지 확인
      5-1. 벗어난 경우 continue
      5-2. 이동 가능하다면 좌표 변경 (x, y = nx, ny)
    6. loop 빠져나오면 최종 위치 출력 
'''


def solution(park, routes):
    # 좌 상 우 하
    direction = {'W': [0, -1], 'N': [-1, 0], 'E': [0, 1], 'S': [1, 0]}

    N, M = len(park), len(park[0])
    x, y = 0, 0

    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                x, y = i, j
                break

    for route in routes:
        d, n = route.split()
        bx, by = x, y  # 백업 x, y 좌표
        dx = direction[d][0]
        dy = direction[d][1]

        for _ in range(int(n)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M) or (park[nx][ny] == 'X'):
                x, y = bx, by
                break
            else:
                x, y = nx, ny

    return [x, y]

# print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))  # [2, 1]
# print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))  # [0, 1]
# print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))  # [0, 0]
