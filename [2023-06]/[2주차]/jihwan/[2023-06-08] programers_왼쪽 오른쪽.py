def solution(str_list):
    answer = []

    for i in str_list:
        if i == "l":
            answer.extend(str_list[:str_list.index("l")])
            break
        elif i == "r":
            answer.extend(str_list[str_list.index("r")+1:])
            break
        else:
            answer.extend([])

    return answer


solution(["u", "u", "l", "r"])
