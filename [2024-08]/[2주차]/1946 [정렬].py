import sys

n = int(sys.stdin.readline())

for i in range(n):
    lst = []
    count = 0
    k = int(sys.stdin.readline())
    for j in range(k):
        lst.append(list(map(int, sys.stdin.readline().split())))

    lst.sort(key=lambda x: x[0])
    grade = lst[0][1]

    for k in lst:
        if grade > k[1]:
            count += 1
            grade = k[1]

    print(count + 1)
