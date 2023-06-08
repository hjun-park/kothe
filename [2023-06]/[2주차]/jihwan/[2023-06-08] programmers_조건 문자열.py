def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        if eval("not "+str(n) + ineq + str(m)):
            answer = 0
        else:
            answer = 1
    else:
        if eval(str(n) + ineq + eq + str(m)):
            answer = 1
        else:
            answer = 0
    return answer


solution(">", "!", 20, 50)
