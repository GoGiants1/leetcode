# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 실제로 다 돌아야하는가?
        
        while head:
            if head.val is None:
                return True
            
            else:
                head.val = None
                head = head.next
            
        return False