from collections import Counter

def solution(strArr):
    answer = 0
    cnt = [0] * 100000
    for i in strArr:
        cnt[len(i)] += 1

    answer = max(cnt)
    return answer

solution(["a","bc","d","efg","hi"])