import datetime


def solution(date1, date2):
    answer = 0

    if (datetime.datetime(date1[0], date1[1], date1[2]) - datetime.datetime(date2[0], date2[1], date2[2])).days >= 0:
        answer = 0
    else:
        answer = 1
    return answer


solution([2021, 12, 28], [2021, 12, 29])
