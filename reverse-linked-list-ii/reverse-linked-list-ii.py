# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # from left to right

        curr = head
        prev = next = None
        curr_idx = 1
        while curr_idx < left:
            prev, curr = curr, curr.next
            curr_idx += 1

        prev_list = prev
        end_reverse = curr
        
        while left <= curr_idx <= right:
            curr.next, curr, prev = prev, curr.next, curr
            curr_idx += 1
        start_reverse = prev
        nxt_list = curr

        if prev_list:
            prev_list.next = start_reverse
        else:
            head = start_reverse
        if end_reverse:
            end_reverse.next = nxt_list

        return head