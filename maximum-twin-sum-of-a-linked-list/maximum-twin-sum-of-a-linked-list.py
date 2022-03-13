# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        mx_sum = -1
        out = []
        while fast:
            out.append(slow.val) 
            fast, slow = fast.next.next, slow.next
        i = -1
        while slow:
            out[i] += slow.val
            i -= 1
            slow = slow.next
        return max(out)