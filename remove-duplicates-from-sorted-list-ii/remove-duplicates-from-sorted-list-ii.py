# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dum_hd = ListNode(val=-102)
        dum_hd.next = ListNode(val=-101)
        dum_hd.next.next = head
        pp, p, c = dum_hd, dum_hd.next, dum_hd.next.next
        dup_cnt = 0
        while c:
            if p.val == c.val:
                c = c.next
                dup_cnt += 1
            else:
                if dup_cnt:
                    pp.next = c
                    dup_cnt = 0
                    p, c = c, c.next
                else:
                    pp, p, c = p, c, c.next
        if dup_cnt:
            pp.next = None
        return dum_hd.next.next