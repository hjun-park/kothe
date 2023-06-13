def solution(board):
    o_cnt = sum([row.count('O') for row in board])
    x_cnt = sum([row.count('X') for row in board])

    # 1. O 선공 다음 X기 때문에 둘 차이는 0혹은 1이다.
    if 0 <= o_cnt - x_cnt <= 1:

        o_win = 0
        x_win = 0
        for i in range(3):
            if board[i] == 'OOO':
                o_win += 1
            elif board[i] == 'XXX':
                x_win += 1

            s = ''
            for j in range(3):
                s += board[j][i]
            if s == 'OOO':
                o_win += 1
            elif s == 'XXX':
                x_win += 1

        diagonal = [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
        o_win += diagonal.count('OOO')
        x_win += diagonal.count('XXX')

        if x_win and o_win: return 0
        if o_win and x_win == 0 and o_cnt == x_cnt: return 0
        if x_win and o_win == 0 and o_cnt != x_cnt: return 0

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
