# 인덱스로 하면 같은 게 있을 경우 제일 앞에 인덱스를 불러오기 때문에 가능

def solution(score):
    lst = []
    for i in score:
        lst.append(sum(i))
    rank = [sorted(lst, reverse=True).index(s) + 1 for s in lst]

    return rank

solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])
