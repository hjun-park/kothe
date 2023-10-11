# dp
def solution(x, y, n):
    d = [1e9] * (y + 1)

    d[x] = 0

    for i in range(x, y + 1):
        if d[i] == 1e9:
            continue
        if i + n <= y:
            d[i + n] = min(d[i + n], d[i] + 1)
        if i * 2 <= y:
            d[i * 2] = min(d[i * 2], d[i] + 1)
        if i * 3 <= y:
            d[i * 3] = min(d[i * 3], d[i] + 1)

    if d[y] == 1e9:
        return -1

    return d[y]
