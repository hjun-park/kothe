# 시간초과 났던 부분
# def solution(players, callings):
#     for call in callings:
#         idx = players.index(call)
#         players[idx - 1], players[idx] = players[idx], players[idx - 1]
#
#     return players

from collections import defaultdict


def solution(players, callings):
    dict_rank = defaultdict(int)
    dict_user = defaultdict(str)
    for i, p in enumerate(players):
        dict_rank[p] = i
        dict_user[i] = p

    for c in callings:
        cur_rank = dict_rank[c]
        target_rank = cur_rank - 1
        cur_user = c
        target_user = dict_user[target_rank]

        dict_user[cur_rank] = target_user
        dict_user[target_rank] = cur_user
        dict_rank[c] = target_rank
        dict_rank[target_user] = cur_rank

    return list(dict_user.values())
