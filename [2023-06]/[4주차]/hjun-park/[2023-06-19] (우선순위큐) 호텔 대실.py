from heapq import heappop, heappush


def solution(book_time):
    answer = 1

    # "HH:MM" → HH * 60 + MM
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time.sort()

    heap = []
    for s, e in book_time:
        if not heap:
            heappush(heap, e + 10)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e + 10)

    return answer

print(
    solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))  # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
