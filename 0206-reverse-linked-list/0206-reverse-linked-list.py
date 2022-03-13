# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursion
        if head is None:
            return head
        def recur(h, new_h):
            if h.next is None:
                new_h = h
                return h, new_h

            new_prev, new_h = recur(h.next, new_h)
            new_prev.next = h
    
            return h, new_h
        last, h = recur(head,None)
        last.next = None
        return h
        # iteration
#         if head is None:
#             return None
#         cur = head
#         prev = None
#         while cur.next:
#             cur.next, cur, prev = prev, cur.next, cur
        
#         if prev:
#             cur.next = prev

#         return cur
        