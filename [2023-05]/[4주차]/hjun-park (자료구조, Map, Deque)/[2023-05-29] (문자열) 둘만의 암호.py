'''
% 26
'''
import string
from collections import defaultdict


def solution(s, skip, index):
    answer = ""
    alpha = list(dict.fromkeys(string.ascii_lowercase, 0))

    for ch in skip:
        if ch in alpha:
            alpha.remove(ch)

    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change

    return answer
