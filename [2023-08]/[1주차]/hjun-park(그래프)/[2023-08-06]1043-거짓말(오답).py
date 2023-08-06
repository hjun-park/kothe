# 1043
'''
4 3
0
2 1 2
1 3
3 2 3 4

3



4 1
1 1
4 1 2 3 4

0




4 1
0
4 1 2 3 4

1


- 과장해서 재밌게 얘기하는 건 좋아하는데 거짓말쟁이는 되기 싫음
- 진실을 아는 사람이 어느 파티든 지민과 같이 있으면 안 됨
- 지민이는 모든 파티에 참가해야 한다.
- 거짓말이 알려지지 않도록 할 수 있는 참가 가능한 최대 파티 개수 구하기


N(사람 수) M(파티 수)
c(이야기 진실을 아는 사람 수) checker(그 사람 번호 리스트)
M개 줄에는 (파티 오는 사람 수) party(파티 오는 사람 번호)

# union-find
1. 진실을 아는 사람들을 먼저 이어준다. 그 다음 부모를 따로 저장한다.
2. 파티 인원 순회하며 파티 인원끼리 이어준다.
3. 다 이었을 때 모두 부모가 같은지 확인한다. 하나라도 같다면 그 파티는 갈 수 없다.
   모두 부모가 다르거나 자신이면 갈 수 있는 파티

'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
checker = list(map(int, input().split()))[1:]
cnt = 0

parent = [-1] * (N + 1)


def find(x):
    if parent[x] < 0:
        return x

    # 경로압축
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if parent[a] < parent[b]:  # a가 부모
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b


if len(checker) != 0:
    first_checker = checker[0]
    for c in checker[1:]:
        union(first_checker, c)


def check_parent():
    for i in range(1, N + 1):
        print(f'{i} parent -> {find(i)}')


for _ in range(M):

    party = list(map(int, input().split()))[1:]
    first_p = party[0]

    for p in party[1:]:
        union(first_p, p)

    for p in party[1:]:
        if find(first_p) == find(p):
            break
    else:
        cnt += 1

    check_parent()

print(cnt)
