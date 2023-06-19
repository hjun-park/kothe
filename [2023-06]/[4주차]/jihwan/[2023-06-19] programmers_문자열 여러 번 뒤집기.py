def solution(my_string, queries):
    answer = ''
    lst = list(my_string)
    for i in queries:
        lst[i[0]: i[1] + 1] = list(reversed(lst[i[0]: i[1] + 1]))
    for i in lst:
        answer += i
    return answer


solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])
