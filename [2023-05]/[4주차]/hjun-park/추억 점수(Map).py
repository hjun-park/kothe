def solution(name, yearning, photo):
    name_dict = {n: y for n, y in zip(name, yearning)}
    answer = []

    for ph in photo:
        cnt = 0
        for p in ph:
            cnt += name_dict.get(p, 0)

        answer.append(cnt)

    return answer

# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
#       [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
