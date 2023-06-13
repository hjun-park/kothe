def solution(board):
    o_cnt = sum([row.count('O') for row in board])
    x_cnt = sum([row.count('X') for row in board])

    # 가로 세로가 바뀐 보드
    reversed_board = [board[0][i] + board[1][i] + board[2][i] for i in range(3)]

    # 1. O 선공 다음 X기 때문에 둘 차이는 0혹은 1이다.
    if 0 <= o_cnt - x_cnt <= 1:
        o_win = 0
        x_win = 0

        # zip을 이용하여 가로 세로 O, X 이긴 횟수를 구함
        for row, reversed_row in zip(board, reversed_board):
            if 'OOO' in [row, reversed_row]:
                o_win += 1
            elif 'XXX' in [row, reversed_row]:
                x_win += 1

        # 대각선
        diagonal = [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
        o_win += diagonal.count('OOO')
        x_win += diagonal.count('XXX')

        # 1. 둘 다 이기는 경우는 없음
        if x_win and o_win: return 0

        # 2. O가 이겼을 때 O와 X는 같을 수 없음
        if o_win and x_win == 0 and o_cnt == x_cnt: return 0

        # 3. X가 이겼을 때 O와 X는 무조건 같아야 함
        if x_win and o_win == 0 and o_cnt != x_cnt: return 0

        # 4. 이외 모두 가능
        return 1
    return 0


print(solution(["O.X", ".O.", "..X"]))  # 1
print(solution(["OOO", "...", "XXX"]))  # 0
print(solution(["...", ".X.", "..."]))  # 0
print(solution(["...", ".O.", "..."]))  # 1
print(solution(["...", "...", "..."]))  # 1
print(solution(["OX.", "OX.", "XO."]))  # 1
print(solution(["OXX", "OXO", "XO."]))  # 1
print(solution(["OXO", "XOX", "OXO"]))  # 1
