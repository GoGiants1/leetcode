# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer
        slow = fast = head
        
        if fast.next is None:
            return fast
        elif fast.next.next is None:
            return fast.next
        
        while fast is not None:
            if fast.next is None:
                break
            else:
                slow, fast= slow.next, fast.next.next
        return slow
            