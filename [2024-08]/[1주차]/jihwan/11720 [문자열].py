import sys

n = int(sys.stdin.readline())
s = str(sys.stdin.readline().strip())

# lst = []
#
# for i in s:
#     lst.append(int(i))
#
# print(sum(lst))


#  다른 풀이 -> 아스키코드를 이용

sum = 0
for i in range(n):
    sum += ord(s[i]) - ord('0')