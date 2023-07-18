def solution(numlist, n):
    result = sorted(numlist, key=lambda x : (abs(x-n), (n-x)))
    # 튜플로 변환하여 정렬
    # 리스트로 해도 괜찮음
    # x = 1, key = (abs(1-4), (4-1)) = (3, 3)
    # x = 2, key = (abs(2-4), (4-2)) = (2, 2)
    # x = 3, key = (abs(3-4), (4-3)) = (1, 1)
    # x = 4, key = (abs(4-4), (4-4)) = (0, 0)
    # x = 5, key = (abs(5-4), (4-5)) = (1, -1)
    # x = 6, key = (abs(6-4), (4-6)) = (2, -2)
    return result


solution([1, 2, 3, 4, 5, 6], 4)
