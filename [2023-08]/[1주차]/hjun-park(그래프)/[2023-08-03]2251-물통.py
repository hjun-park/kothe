# 2251

'''
문제
각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다.
처음에는 앞의 두 물통은 비어 있고,
세 번째 물통은 가득(C 리터) 차 있다.
이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데,
이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
이 과정에서 손실되는 물은 없다고 가정한다.

이와 같은 과정을 거치다보면
세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다.
첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는
물의 양을 모두 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, C가 주어진다.

출력
첫째 줄에 공백으로 구분하여 답을 출력한다. 각 용량은 오름차순으로 정렬한다.

예제 입력 1
8 9 10
예제 출력 1
1 2 8 9 10
'''

'''

1. (A, B, C)를 하나의 노드로 본다.
2. input_a=input_b=0, input_c는 입력 받은 값으로 초기화
    - now = [input_a, input_b, input_c]
    - answer = [False for _ in range(201)]  # 순서대로 출력하기위해 미리 변수로 선언
3. 추가적으로 아래 초기화
    - visited 201개까지 초기화 (2차원)
    - d_snd, d_rcv 초기화 ( 0, 1, 2 로 구성 )
3. BFS 시작
    q 초기화
    q에 0, 0 append ( 0 -> 0으로 시작)
    0, 0에 대해 방문처리 (d_snd, d_rcv)
    answer에 C 값을 추가 
    while q:
        A, B, _ = q.popleft()
        C = input_c - B - A

        # 6방향 순회(k) 
            # next = [A, B, C]
            # next[d_rcv[k]] += next[d_snd[k]] # 받는 쪽에서 보내는 쪽 나눠가짐
            # 보내는 쪽은 0이 됨
            # 근데, 만약 물이 넘칠 때 (즉, now[rcv[k]] 보다 next가 더 크다면)
                # next의 받은 쪽 k위치에서 now 받는 쪽 k만큼 뺀 이후 보내는 쪽에 반영
                # 다시 next 받는 쪽은 최대치인 now 받는 쪽 값으로 대입
            # 근데, 만약 A, B 물의 양이 없던 값일 때,
                # 방문처리하고, q에 집어넣음
                # 근데, 만약 문제에서 요구하는 A 무게가 0이라면
                    # 정답에 C 무게값 assign 




answer 순회하면서 true인 것만 출력

'''

# 물통의 상태 (A, B, C)를 하나의 노드로 보고 BFS 돌리기
import sys
from collections import deque

input = sys.stdin.readline

# 입력받을 물통의 사이즈
size = list(map(int, input().split()))
# A, B가 비어있을 때 C의 값을 담을 배열
# 정답을 미리 배열로 만들어놓는 이유는 순서대로 출력하는 것이 문제 요구사항이기 때문
answer = [False] * 201
# A, B가 특정 값일 때 방문했는지 여부를 판단하는
visited = [[False] * 201 for _ in range(201)]

# dx, dy처럼 (A->B, A->C, B->A, B->C, C->A, C->B)
# 6방향으로 물을 주는 케이스 (그래프 분기 케이스)
d_snd = [0, 0, 1, 1, 2, 2]
d_rcv = [1, 2, 0, 2, 0, 1]


def bfs():
    # 1. 큐 선언
    q = deque()
    # 2. A, B 초기화, A,B만 하는 이유는 visited가 2차원 배열이기 때문
    q.append([0, 0])
    # 3. A, B 0에 대해서 우선 방문처리
    visited[0][0] = True
    # 4. A, B가 문제에서 요구하는 0을 가지기 때문에 일단 C의 값을 True
    answer[size[2]] = True
    # 5. BFS 순환
    while q:
        # 1. A, B 빼기
        A, B = q.popleft()

        # 2. C는 전체 물의 양에서 - B - A 한 경우
        # 최초 C에만 물이 담겨있었기 때문에 계속해서 이런 방식으로 물의 양을 구한다.
        C = size[2] - B - A

        # 6번 순회
        for d in range(6):
            # 1. 현재 노드 설정
            now = [A, B, C]

            # 2. 물을 붓는다. rcv가 snd의 물을 받는다.
            #    물을 부었기 때문에 snd 쪽은 0이다
            now[d_rcv[d]] += now[d_snd[d]]
            now[d_snd[d]] = 0

            # 3. 근데, 물을 부었는데 받는 쪽(rcv)가 넘친다면
            if now[d_rcv[d]] > size[d_rcv[d]]:
                # 1. 넘친 만큼은 물을 준(snd) 쪽으로 다시 준다.
                #    기존 받은 쪽은 자신의 최댓값만 만큼만 취급한다.
                #     서로 바뀌어도 상관 없다.
                now[d_snd[d]] = now[d_rcv[d]] - size[d_rcv[d]]
                now[d_rcv[d]] = size[d_rcv[d]]

            # 4. 물을 주었는데 A, B가 이전에 없던 값이라면
            if not visited[now[0]][now[1]]:
                # 1. 방문처리 + 큐에 담기
                visited[now[0]][now[1]] = True
                q.append([now[0], now[1]])

                # 2. 만약 문제에서 요구한대로 A가 0이라면
                if now[0] == 0:
                    # 1. 현재 C의 물통 값을 True로 변경
                    answer[now[2]] = True


bfs()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')
