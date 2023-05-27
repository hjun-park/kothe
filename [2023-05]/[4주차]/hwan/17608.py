n = int(input())
lst = []
cnt = 1

for i in range(n):
    lst.append(int(input()))
max_num = lst[-1]

for i in range(len(lst) - 1, -1, -1):
    if lst[i] > max_num:
        cnt += 1
        max_num = lst[i]

print(cnt)
