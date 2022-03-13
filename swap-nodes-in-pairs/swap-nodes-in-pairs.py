# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy_head = ListNode()
        dummy_head.next = head
        
        prev_set = dummy_head
        prev = head
        curr = head.next
        if curr is None:
            return head
        
        while curr and prev:
            prev.next, curr.next = curr.next, prev
            prev_set.next = curr
            prev_set, prev = prev, prev.next
            if prev is not None:
                curr = prev.next
            else:
                curr = None
        if prev:
            prev_set.next = prev    
            
        
        return dummy_head.next

        # # If the list has no node or has only one node left.
        # if not head or not head.next:
        #     return head

        # # Nodes to be swapped
        # first_node = head
        # second_node = head.next

        # # Swapping
        # first_node.next  = self.swapPairs(second_node.next)
        # second_node.next = first_node

        # # Now the head is the second node
        # return second_node