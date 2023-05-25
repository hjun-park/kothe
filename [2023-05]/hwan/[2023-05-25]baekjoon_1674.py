import sys

n, m = map(int, sys.stdin.readline().split(" "))

lst = []
for i in range(n + m):
    lst.append(str(sys.stdin.readline().strip()))

not_see = set(lst[:n])
not_listen = set(lst[m:])

result = sorted(list(not_see.intersection(not_listen)))

print(len(result), "\n".join(result), sep="\n")
