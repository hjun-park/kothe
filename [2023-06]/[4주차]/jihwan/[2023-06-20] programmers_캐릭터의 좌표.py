def solution(keyinput, board):
    answer = []
    width = board[0] // 2
    height = board[1] // 2
    rst_width = 0
    rst_height = 0
    for i in keyinput:
        if i == "left":
            if rst_width > -width:
                rst_width -= 1
        elif i == "right":
            if rst_width < width:
                rst_width += 1
        elif i == "up":
            if rst_height < height:
                rst_height += 1
        elif i == "down":
            if rst_height > -height:
                rst_height -= 1


    answer.append(rst_width)
    answer.append(rst_height)

    return answer


solution(["down", "down", "down", "down", "down"], [3,0])