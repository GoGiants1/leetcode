# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Mine, OOP style
        
#         while head:
#             if hasattr(head, "visited"):
#                 return head
#             else:
#                 setattr(head, "visited", True)
            
#             head = head.next
        
#         return None
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None