def solution(n, lost, reserve):
    cnt = n
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    for i in new_lost:
        if i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        elif i + 1 in new_reserve:
            new_reserve.remove(i + 1)
        else:
            cnt -= 1
    return cnt


solution(7, [5, 1, 4], [1, 2, 5, 3])
