# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        stack = []
        node_list = []
        new_head = None
        
        prev, curr = None, head
        while curr:
            if len(stack) == k:
                node_list.append(stack)
                stack = []
            
            stack.append(curr)
            
            curr = curr.next
        if len(stack):
            node_list.append(stack)
        

        last_node = None
        for st in node_list:
            if new_head is None:
                new_head = st[-1]
            if last_node:
                if len(st) == k:
                    last_node.next = st[-1]
                else:
                    last_node.next = st[0]
                    break

            if len(st) == k:
                prev = None
                curr = None
                while st:
                    curr = st.pop()
                    if prev:
                        prev.next = curr
                    prev = curr
                    
                last_node = prev
                last_node.next = None

        return new_head
        

        