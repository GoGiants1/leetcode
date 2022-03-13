"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        self.d_hd = Node(x=0)

        curr_origin = head
        curr_cp = self.d_hd


        while curr_origin:
            new_node = Node(x= curr_origin.val, random=curr_origin.random)
            curr_cp.next, curr_cp = new_node, new_node
            curr_origin.next, curr_origin = new_node, curr_origin.next
            
        
        curr_cp = self.d_hd.next
        while curr_cp:
            if curr_cp.random:
                curr_cp.random = curr_cp.random.next
            curr_cp = curr_cp.next

        return self.d_hd.next
            
