import sys


def solution(n: int) -> str:
    result = []
    for i in range(n):
        stack = []
        vps = str(sys.stdin.readline())
        for j in vps:
            if j == "(":
                stack.append(j)
            elif j == ")":
                if stack:
                    stack.pop()
                else:
                    result.append("NO")
                    break
        else:
            if not stack:
                result.append("YES")
            else:
                result.append("NO")
    return '\n'.join(result) # 줄 바꿈형식으로 리턴을 해야 하므로


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(solution(n))
