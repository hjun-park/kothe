# // 1717 - 집합의 표현
'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

N, M = map(int, input().split())


# 1) 부모노드 초기화 (-1로 초기화, 음수는 높이, 양수는 부모 노드번호, 즉, 음수라면 부모노드라는 것을 의미)

# 2) c, a, b를 입력 받는다 (c는 1, 0 (union or find), a, b는 합집합 대상)

# 2-1) 만약 c가 0이라면 union(a, b)
# 2-2) 만약 c가 1이라면 find(a) find(b) 통해 a와 b의 부모가 같은지 확인한다. 다르면 NO, 같다면 YES 출력

# 3) def union(a, b)
#   - 각 부모를 찾는다.
#    - 만약 부모가 같다면 합치지 않고 return
#    - 부모가 다르다면 해당 부모가 가지고 있는 depth를 둘 다 구함
#   - depth를 비교해서 depth 큰 쪽으로 작은 depth가 들어가야 한다.
#       - 부모를 재설정하고 자식이 부모로 들어갔으니 그 부모의 depth는 더 커져야 한다.

# 4) def find(a)
#    - 만약 부모가 음수라면 높이를 표현하는 것이고 이는 곧 부모기때문에 본인의 부모 그대로 return 한다.
#   - 음수가 아니라면 find()에 부모를 넣고 경로압축을 진행한다.
#   - 경로압축 진행 후 그 부모값을 return 한다.


def find(x):
    # 1. 음수라면 높이값을 갖고 있는 것이며 이는 곧 자신이 부모라는 의미
    if parent[x] < 0:
        return x

    # 2. 경로압축 후 부모 반환
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if parent[a] < parent[b]:  # A의 높이가 더 큰 경우 즉, A가 부모가 되는 경우
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b


parent = [-1] * (N + 1)
# parent[0] = 0

for _ in range(M):
    c, a, b = map(int, input().split())

    if not c:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
