import re


def solution(myStr):
    answer = []
    myStr = re.split("[abc]", myStr.strip())

    for i in myStr:
        if i != "":
            answer.append(i)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer

solution("baconlettucetomato")