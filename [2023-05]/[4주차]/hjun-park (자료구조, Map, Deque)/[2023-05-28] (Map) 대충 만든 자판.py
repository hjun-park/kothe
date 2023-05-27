from collections import defaultdict


def solution(keymap, targets):
    type_map = defaultdict(int)
    answer = []

    for key in keymap:
        for i, k in enumerate(key):
            type_map[k] = i + 1 if type_map[k] == 0 else min(type_map[k], i + 1)

    for target in targets:
        cnt = 0
        for t in target:
            tp = type_map.get(t)
            if tp is None:
                cnt = -1
                break
            else:
                cnt += tp
        answer.append(cnt)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
