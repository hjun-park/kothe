# enumerate 를 사용하여 인덱스와 num 값을 동시에 비교

def solution(arr, idx):
    answer = -1
    for i, num in enumerate(arr):
        if idx <= i and num == 1:
            return i

    return answer

solution([1, 0, 0, 1, 0, 0], 3)