# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_out = curr = ListNode()
        carry = 0

        while l1 or l2:
            tmp = 0
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            s, r = divmod(tmp + carry, 10)
            carry = s
            curr.next = ListNode(val=r)
            curr = curr.next
        
        if carry:
            curr.next = ListNode(val=carry)
        return dummy_out.next
            
        

        
        
            