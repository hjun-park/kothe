import sys
#
# lst = [0] * 10
#
# for i in range(10):
#     lst[i] = int(sys.stdin.readline()) % 42
#
# print(len(set(lst)))


# 다른 풀이 (체크 배열) -> 런타임 에러가 나오기는 하는데 이런 방법도 있다~

lst = [0] * 42

for i in range(10):
    index = int(sys.stdin.readline())
    lst[index % 42] = 1

print(sum(lst))