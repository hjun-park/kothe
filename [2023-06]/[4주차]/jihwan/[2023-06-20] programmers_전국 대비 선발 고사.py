def solution(rank, attendance):
    answer = 0
    lst = dict(zip(rank, attendance))
    idx = []
    rst = []
    for key, value in lst.items():
        if value:
            idx.append(key)

    for i in sorted(idx)[:3]:
        rst.append(rank.index(i))
    answer = rst[0] * 10000 + rst[1] * 100 + rst[2]
    return answer


solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False])
