# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def next_val_node(node: Optional[ListNode]):
            if node:
                while node.next and node.next.val == node.val:
                    node = node.next

            return node
        head = None
        if not (list1 and list2):
            return list1 if list1 else list2
        
        if not(list1 or list2):
            return list1
        
        if list1.val < list2.val:
            head , list1 = list1, list1.next
        else:
            head , list2 = list2, list2.next


        curr = head

        while list1 and list2:
#             list1 = next_val_node(list1)
#             list2 = next_val_node(list2)
            
            if list1.val < list2.val:
                curr.next, list1 = list1, list1.next
            else:
                curr.next, list2 = list2, list2.next
            
            curr = curr.next
            
        if list1:
            curr.next = list1
        
        elif list2:
            curr.next = list2
        return head