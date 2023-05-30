from collections import defaultdict


# 딕셔너리에서 인덱스를 항상 최신으로 유지 (i-_dict[s[i]])
def solution(s):
    answer = []
    _dict = defaultdict(lambda: -1)

    for i in range(len(s)):
        if _dict[s[i]] == -1:
            answer.append(-1)
        else:
            answer.append(i - _dict[s[i]])

        _dict[s[i]] = i

    return answer


print(solution("banana"))  # [-1, -1, -1, 2, 2, 2]
print(solution("foobar"))  # [-1, -1, 1, -1, -1, -1]
