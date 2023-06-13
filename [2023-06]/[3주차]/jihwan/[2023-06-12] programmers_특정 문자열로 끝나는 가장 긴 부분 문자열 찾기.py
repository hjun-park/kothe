def solution(myString, pat):
    answer = ''

    answer = myString[0: myString.rindex(pat) + len(pat)]

    return answer

solution("AbCdEFG", "dE")