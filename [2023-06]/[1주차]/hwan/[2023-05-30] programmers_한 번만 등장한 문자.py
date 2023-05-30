import collections

def solution(s):
    answer = ''
    value = list(collections.Counter(s).values())
    key = list(collections.Counter(s).keys())
    lst = []

    for i in range(len(value)):
        if value[i] == 1:
            lst.append(key[i])
    for i in sorted(lst):
        answer += str(i)

    return answer
