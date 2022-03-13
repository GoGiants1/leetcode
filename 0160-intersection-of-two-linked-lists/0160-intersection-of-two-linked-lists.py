# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        sol 1
        # two hash map
        a_hash = {}
        b_hash = {}
        a_idx = 0
        b_idx = 0
        while headA:    
            a_hash[a_idx], headA = headA, headA.next
            a_idx += 1
        while headB:
            b_hash[b_idx], headB = headB, headB.next
            b_idx += 1
        last_inter_node = None
        while a_hash and b_hash:
            a_idx, a = a_hash.popitem()
            b_idx, b = b_hash.popitem()
            if a == b:
                last_inter_node = a
            else:
                break
        
        return last_inter_node
        '''
    
        '''
        
        a_head = headA
        b_head = headB
        
        stack = set()
        while headA:    
            stack.add(headA)
            headA =  headA.next
        
        while headB:
            if headB in stack:
                return headB
            headB = headB.next
        return None
        
        '''
        # sol 2 fast but memory too big 
#         a_list = []
#         b_list = []
#         while headA:
#             a_list.append(headA)
#             headA = headA.next
            
#         while headB:
#             b_list.append(headB)
#             headB = headB.next
        
#         last_inter = None
#         for a, b in zip(reversed(a_list), reversed(b_list)):
#             if a == b:
#                 last_inter = a
#             else:
#                 break
#         return last_inter
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.
