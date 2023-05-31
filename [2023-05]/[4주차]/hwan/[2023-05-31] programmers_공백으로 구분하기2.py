def solution(my_string):
    answer = []
    lst = my_string.split(" ")

    for i in lst:
        if len(i.split()) > 0:
            answer.append(i)

    return answer

solution(" i    love  you")