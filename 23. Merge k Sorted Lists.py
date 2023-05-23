from heapq import heappush, heappop
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        rst, root = ListNode(None), ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            cur_node = heappop(heap)
            idx = cur_node[1]
            rst.next = cur_node[2]
            rst = rst.next

            if rst.next:
                heappush(heap, (rst.next.val, idx, rst.next))

        return root.next
