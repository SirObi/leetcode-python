# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = []

        # use unique_key, so that heapq doesn't try to sort on a ListNode object (no __cmp__, so error)
        unique_key = 0
        for _list in lists:
            while _list:
                heappush(queue, (_list.val, unique_key, _list))
                _list = _list.next
                unique_key += 1

        start_node_ref = ListNode()
        merged = start_node_ref

        while len(queue) > 0:
            merged.next = heappop(queue)[2]
            merged = merged.next

        return start_node_ref.next
