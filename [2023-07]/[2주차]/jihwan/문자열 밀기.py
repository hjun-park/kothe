# A 끝자리를 앞으로 빼고 끝자리를 제외한 나머지 문자열을 더하는 식으로 하여 같으면 리턴 cnt값이 사이즈값이랑 같으면 -1 리턴

def solution(A, B):
    cnt = 0
    while cnt != len(A):
        if A == B:
            return cnt
        A = A[-1] + A[:-1]
        cnt += 1

    return -1


print(solution("hello", "ohell"))
