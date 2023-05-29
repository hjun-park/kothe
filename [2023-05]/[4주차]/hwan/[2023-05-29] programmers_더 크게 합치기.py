def solution(a, b):
    answer = 0
    type1 = int(str(a) + str(b))
    type2 = int(str(b) + str(a))

    if type1 > type2:
        answer = type1
    else:
        answer = type2
    return answer

