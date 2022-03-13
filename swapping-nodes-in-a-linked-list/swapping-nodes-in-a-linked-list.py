# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head

        dq = deque()
        first_k = None
        end_k = None
        idx = 1
        while head:
            if idx == k:
                first_k = head
                end_k = first
            elif idx > k:
                end_k = end_k.next
            idx += 1
            head = head.next
            
        first_k.val, end_k.val = end_k.val, first_k.val

        return first