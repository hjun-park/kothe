'''
1. 4면(위, 아래, 왼쪽, 오른쪽)에 대해서 쿠션을 넣었을 때 거리의 최솟값의 제곱을 구한다.
2. 같은 선 상이라서 쿠션을 못 넣는 경우는 제외한다.
'''


def solution(m, n, startX, startY, balls):
    answer = []

    # m : 가로 길이
    # n : 세로 길이
    for ball in balls:
        diffX = startX - ball[0]  # X 차이
        diffY = startY - ball[1]  # Y 차이

        left = (startX + ball[0]) ** 2 + (diffY ** 2)  # 왼쪽 쿠션
        right = ((m - startX) + (m - ball[0])) ** 2 + (diffY ** 2)  # 오른쪽 쿠션
        top = ((n - startY) + (n - ball[1])) ** 2 + (diffX ** 2)  # 위 쿠션
        bottom = (startY + ball[1]) ** 2 + (diffX ** 2)  # 아래 쿠션

        # 오른쪽 쿠션

        if diffX == 0:  # x선 상에 같이 놓였다면
            if diffY > 0:  # 타겟 공이 시작점보다 아래에 있다면 아래 쿠션 X
                dist = min(left, right, top)
            else:  # 위 쿠션 X
                dist = min(left, right, bottom)
        elif diffY == 0:  # y선 상이 같다면
            if diffX > 0:  # 타겟 공이 시작점보다 왼쪽에 있다면 왼쪽 쿠션 X
                dist = min(right, top, bottom)
            else:  # 오른쪽 쿠션 X
                dist = min(left, top, bottom)
        else:
            dist = min(left, right, top, bottom)

        answer.append(dist)

    return answer


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
