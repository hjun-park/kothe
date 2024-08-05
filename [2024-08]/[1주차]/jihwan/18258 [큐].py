from collections import deque
import sys

n = int(sys.stdin.readline())

que = deque()

for i in range(n):
    lst = list(sys.stdin.readline().strip().split(' '))
    if lst[0] == "push":
        que.append(lst[1])
    if lst[0] == "front":
        if len(que) == 0:
            print("-1")
        else:
            print(que[0])
    if lst[0] == "back":
        if len(que) == 0:
            print("-1")
        else:
            print(que[-1])
    if lst[0] == "size":
        print(len(que))
    if lst[0] == "pop":
        if len(que) == 0:
            print("-1")
        else:
            print(que.popleft())
    if lst[0] == "empty":
        if len(que) == 0:
            print("1")
        else:
            print("0")
