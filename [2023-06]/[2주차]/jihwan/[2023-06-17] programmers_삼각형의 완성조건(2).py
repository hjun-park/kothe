def solution(sides):
    answer = 0
    sides.sort()
    for i in range(0, sides[1] + 1):
        if sides[0] + i > sides[1]:
            answer += 1
    answer += sum(sides) - 1 - sides[1]

    return answer
