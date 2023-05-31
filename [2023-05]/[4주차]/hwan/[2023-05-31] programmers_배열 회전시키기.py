def solution(numbers, direction):
    answer = [0] * len(numbers)
    if direction == "right":
        answer[0] = numbers[len(numbers) - 1]
        for i in range(1, len(numbers)):
            answer[i] = numbers[i - 1]
    else:
        answer[len(numbers) - 1] = numbers[0]
        for i in range(0, len(numbers) - 1):
            answer[i] = numbers[i + 1]

    return answer

solution([4, 455, 6, 4, -1, 45, 6]	, "left")