# from collections import deque

def solution(cards1, cards2, goal):

    # cards1 = deque(cards1)

    # cards2 = deque(cards2)

    

    while goal:

        if cards1 and (cards1[0] == goal[0]):

            cards1.pop(0)

            goal.pop(0)

        elif cards2 and (cards2[0] == goal[0]):

            cards2.pop(0)

            goal.pop(0)

        else:

            return "No"

        

    

    return "Yes"

