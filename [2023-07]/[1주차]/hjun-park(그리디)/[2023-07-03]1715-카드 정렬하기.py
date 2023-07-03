import sys
from heapq import heapify, heappush, heappop

input = sys.stdin.readline

N = int(input().rstrip())
cards = [int(input().rstrip()) for _ in range(N)]

heapify(cards)

rst = 0
while len(cards) > 1:
    a = heappop(cards)
    b = heappop(cards)

    temp = a + b
    rst += temp
    heappush(cards, temp)

print(rst)
