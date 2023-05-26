def solution(my_string, indices):
    my_string = list(my_string)

    indices.sort(reverse=True)
    for i in indices:
        my_string.pop(i)

    answer = "".join(my_string)

    return answer

solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3])
