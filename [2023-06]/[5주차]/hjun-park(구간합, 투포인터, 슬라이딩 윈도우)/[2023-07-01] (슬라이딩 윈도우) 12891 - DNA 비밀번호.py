import sys
from collections import defaultdict

input = sys.stdin.readline


def is_secret():
    for p, c in zip(pass_dict.values(), check_dict.values()):
        if c < p:
            return False
    return True


S, P = map(int, input().split())
DNA = list(input().rstrip())
min_a, min_c, min_g, min_t = map(int, input().split())
pass_dict = defaultdict(int)

pass_dict['A'] = min_a
pass_dict['C'] = min_c
pass_dict['G'] = min_g
pass_dict['T'] = min_t

check_dict = defaultdict(int)

check_dict['A'] = DNA[0:P].count('A')
check_dict['C'] = DNA[0:P].count('C')
check_dict['G'] = DNA[0:P].count('G')
check_dict['T'] = DNA[0:P].count('T')

cnt = 0
left, right = 0, P - 1

while right < S:
    if is_secret():
        cnt += 1

    if right >= S:
        break

    check_dict[DNA[left]] -= 1
    left += 1
    right += 1
    if right < S:
        check_dict[DNA[right]] += 1

print(cnt)
