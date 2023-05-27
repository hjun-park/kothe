import sys

## 처음 실행 했던 것 -> 하지만 시간초과 (pypy3로 할 경우 10% 까진 올라감)

# n = int(sys.stdin.readline().strip())
# lst = list(map(int, sys.stdin.readline().split(" ")))
# n1 = int(sys.stdin.readline().strip())
# compare = list(map(int, sys.stdin.readline().split(" ")))
#
# for i in lst:
#     if i in compare:
#         print(1)
#     else:
#         print(0)

## 두번째 실행 -> 컴프리헨션을 통하여 좀 더 빠르게 구현 (pypy3로 할 경우 25%까진 올라감)
# n = int(sys.stdin.readline().strip())
# lst = list(map(int, sys.stdin.readline().split(" ")))
# n1 = int(sys.stdin.readline().strip())
# compare = list(map(int, sys.stdin.readline().split(" ")))
#
# [print(1) if i in lst else print(0) for i in compare]

## 결국 짜증나서 gpt 한테 속도 개선만 해달라고 함 -> 정답
## 원래는 이분탐색으로 해야한다고 함

n = int(sys.stdin.readline().strip())
lst = set(map(int, sys.stdin.readline().split(" ")))
n1 = int(sys.stdin.readline().strip())
compare = list(map(int, sys.stdin.readline().split(" ")))

for i in lst:
    if i in compare:
        print(1)
    else:
        print(0)

# 설명: 일반적으로 set은 list보다 작업이 빠름 -> 집합은 요소를 저장하기 위해 해시 기반 인덱싱을 사용, 리스트는 요소를 확인하기 위해 각 요소를 반복해야함
# 다만 set은 중복허용을 하지 않고 정렬이 되지 않음
# 중복을 허용하지 않고 요소 확인하는 경우 set을 활용하는 것도 좋음