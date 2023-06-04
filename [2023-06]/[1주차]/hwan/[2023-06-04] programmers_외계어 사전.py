from itertools import permutations

def solution(spell, dic):
    answer = 0

    lst = list(permutations(spell, len(spell)))
    perList = []
    for i in lst:
        perList.append("".join(i))
    for i in perList:
        if i in dic:
            answer = 1
            break
        else:
            answer = 2

    return answer