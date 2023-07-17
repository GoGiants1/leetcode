# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # reverse nodes

        # add up to msb

        def reverse_nodes(root: ListNode | None)-> ListNode | None:
            if root is None:
                return None
            
            prev, curr = None, root
            length = 0
            while curr is not None:
                curr.next, curr, prev = prev, curr.next, curr
                length += 1
            return prev, length
        
        (l1, l1_len), (l2, l2_len) = reverse_nodes(l1), reverse_nodes(l2)
        if l2_len > l1_len:
            l1, l2 = l2, l1
        carry = 0
        curr = l1
        while curr:
            if l2:
                carry += l2.val
            carry, curr.val = divmod(curr.val + carry, 10)

            curr = curr.next
            if l2:
                l2 = l2.next
        new_l1 , _ =  reverse_nodes(l1)
        if carry > 0:
            msd =  ListNode(val=carry)
            msd.next = new_l1
        else:
            msd = new_l1
        return msd
        


