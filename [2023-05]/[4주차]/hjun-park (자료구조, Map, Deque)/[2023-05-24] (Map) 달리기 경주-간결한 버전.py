def solution(players, callings):
    # 1) { 'hjun-park' : 0, 'hwan' : 1 } 처럼 구성
    player_idx_dict = {player: index for index, player in enumerate(players)}

    # 2) 부른 사람들 리스트 순회
    for j in callings:
        # 1) 불린 대상 순서와 그 앞에 있는 사람의 인덱스 가져옴
        cur_idx = player_idx_dict[j]
        target_idx = cur_idx - 1

        # 조건에 걸리지 않기 때문에 필요없음
        # if cur_idx > 0 and players[target_idx] != j:

        # 2) 이전 답은 map을 2개 만들었지만 여기서는 players를 하나의 map으로 사용했다.
        players[cur_idx], players[target_idx] = players[target_idx], players[cur_idx]

        # 3) 순위 재설정
        player_idx_dict[players[cur_idx]] = cur_idx
        player_idx_dict[players[target_idx]] = target_idx
