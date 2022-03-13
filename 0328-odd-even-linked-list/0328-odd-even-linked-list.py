# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or  head.next is None or head.next.next is None:
            return head
        h = odd = head
        even_head = even = head.next
        
        is_odd = True
        head = head.next.next
        
        while head:
            if is_odd == True:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
            head = head.next
            is_odd = not is_odd
        
        odd.next, even.next = even_head, None
        return h