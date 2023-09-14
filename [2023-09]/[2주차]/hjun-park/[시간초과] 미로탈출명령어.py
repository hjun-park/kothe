'''
 시간초과 사유
 -> dllru 경로가 존재하는경우 dlu 방향 탐색는 필요 없음 (https://velog.io/@chocochip/2023-KAKAO-BLIND-RECRUITMENT-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%92%80%EC%9D%B4)

 https://comdoc.tistory.com/entry/%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4
 https://dhalsdl12.tistory.com/284 (추천 BFS)

'''


'''
/*
    n, m
    시작 : x,y
    도착 : r,c
    목표 : 시작 -> 도착

    조건
    1) 바깥 나갈 수 없음
    2) (x, y) -> (r, c) 이동거리 = k
      -> 출발 도착지를 포함해 두 번 이상 방문가능
    3) 문자열이 사전순으로 가장 빠른 경로를 출력, 없다면 impossible 출력

    이동경로 문자 : l, r, u, d

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]


    제약조건 고민
    1) 두 번 이상 방문 가능
      -> 방문체크할 필요없음

    2) 종료조건은 언제 ?
      -> k번 이동했을 때
      -> 즉, k번 이동했을 때 현재 좌표를 보면 된다.
      -> 뺑뻉이 돌텐데? -> k번 이상 진행될 수 없기에 끝은 있다.

    3) queue에 들어갈 내용은 ?
      -> x, y, cnt, 좌표리스트




    [슈도코드]
    from collections import deque

    def solution(n, m, x, y, r, c, k):

        graph = [[0] * m for _ in range(n)]
        start = (x, y)
        end = (r, c)
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        direction = {0: 'l', 1: 'u', 2: 'r', 3: 'd'}
        answer = []

        def bfs():
            # q에 정보 집어넣기 (start[0], start[1], 0, [])
            q = deque()
            q.append([start[0], start[1], 0, list()])

            while q:
                qx, qy, cnt, path = q.popleft()

                if cnt == k and qx == end[0] and qy == end[1]:
                    answer.append(path)
                    continue

                if cnt == k? 그리고 꺼낸x,y == end ?
                    answer.append[꺼낸경로]
                    continue

                for i -> 4:
                    nx, ny 지정
                    nx, ny가 범위에 넘지 않는다면
                    꺼낸경로.append(direction[d])
                    q.append((nx, ny, cnt + 1, 꺼낸경로))


        return sorted(answer)[0]


*/
'''

from collections import deque


def solution(n, m, x, y, r, c, k):
    # graph = [[0] * m for _ in range(n)]
    start = (x - 1, y - 1)
    end = (r - 1, c - 1)
    # 하, 좌, 우, 상
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    direction = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}

    # dx = [0, 1, 0, -1]
    # dy = [-1, 0, 1, 0]
    # direction = {0: 'l', 1: 'u', 2: 'r', 3: 'd'}
    answer = []

    def bfs():
        q = deque()
        q.append([start[0], start[1], 0, ''])

        while q:
            qx, qy, cnt, path = q.popleft()

            if cnt > k:
                continue

            if cnt == k and qx == end[0] and qy == end[1]:
                answer.append(path)
                continue

            for d in range(4):
                nx = qx + dx[d]
                ny = qy + dy[d]

                if 0 <= nx < n and 0 <= ny < m:
                    q.append([nx, ny, cnt + 1, path + direction[d]])

    bfs()
    # sorted 에서 시간초과
    # print(answer)
    return 'impossible' if len(answer) == 0 else answer[0]


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))

# assert solution(3, 4, 2, 3, 3, 1, 5) == 'dllrl'
# assert solution(2, 2, 1, 1, 2, 2, 2) == 'dr'
