def solution(name, yearning, photo):
    answer = []
    dic = [pair for pair in zip(name, yearning)]

    for j in photo:
        total = 0
        for i in dic:
            if i[0] in j:
                total += i[1]

        answer.append(total)
    return answer


solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
         [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
