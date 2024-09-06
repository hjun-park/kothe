import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
sum = 0
for i in range(n):
    # 본인 포함 다른 사람에게 자신의 시간을 할당하기 때문
    sum += (n - i) * lst[i]

print(sum)