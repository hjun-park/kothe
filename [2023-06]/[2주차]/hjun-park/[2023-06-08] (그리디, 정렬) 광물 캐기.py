'''
[정렬, 그리디]
 - 곡괭이는 5번 연속으로 사용해야 한다. / 최대한 다이아 곡괭이로 다이아가 많은 광석을 캐야 한다.
 - 즉, 광물을 5개씩 묶은 후 다이아가 많은 게 먼저 오도록 정렬, 이후 곡괭이만큼 처리
 - 데이터 범위는 크지 않음

[테스트 케이스 8번 고려]
- 곡괭이가 광물을 다 캐지 못할 때, 굳이 무리해서 피로도가 높은 것을 캘 필요가 없다.
- 즉, slicing을 곡괭이 상황에 고려해서 하면 된다.
'''


def solution(picks, minerals):
    answer = 0
    pick_dict = [{"diamond": 1, "iron": 1, "stone": 1},
                 {"diamond": 5, "iron": 1, "stone": 1},
                 {"diamond": 25, "iron": 5, "stone": 1}]

    dia_pick, iron_pick, stone_pick = picks

    # # 테스트케이스 8번 X
    # minerals = [minerals[i:i + 5] for i in range(0, 5 * len(minerals), 5)]

    # 테스트케이스 8번 고려 (곡괭이가 캘 수 있는 광물까지만 slicing 한다)
    minerals = [minerals[i:i + 5] for i in range(0, 5 * sum(picks), 5)]

    minerals.sort(key=lambda x: (-x.count("diamond"), -x.count("iron")))
    print(minerals)

    for mineral in minerals:
        if dia_pick:
            for m in mineral:
                answer += pick_dict[0][m]
            dia_pick -= 1
        elif iron_pick:
            for m in mineral:
                answer += pick_dict[1][m]
            iron_pick -= 1
        elif stone_pick:
            for m in mineral:
                answer += pick_dict[2][m]
            stone_pick -= 1

    return answer


print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1],
               ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron",
                "diamond"]))
