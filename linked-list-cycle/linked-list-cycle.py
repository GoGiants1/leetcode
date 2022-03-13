# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # My sol 1.
        # fast = slow = head

        # while slow:
        #     if slow.val == math.inf:
        #         return True
        #     slow.val, slow = math.inf, slow.next

        # return False

        # Sol 2: floyd
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True