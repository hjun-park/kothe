import sys

s = str(sys.stdin.readline())
for i in range(26):
    print(s.find(chr(97 + i)), end=" ")