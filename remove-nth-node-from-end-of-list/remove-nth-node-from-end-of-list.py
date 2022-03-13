# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Sol 1
        # cur = head
        # total = 1
        # while cur.next:
        #     cur = cur.next
        #     total += 1


        
        # cur = head
        # prev = head

        # target = total - n
        # if target == 0:
        #     return head.next

        # while target:
        #     prev, cur = cur, cur.next
        #     target -= 1
        # prev.next = cur.next

        # return head

        d = {}

        cur = head
        idx = 1

        while cur:
            d[idx], cur = cur, cur.next
            idx += 1
        t = idx - n
        if t - 1 in d and t + 1 in d:
            d[t - 1].next = d[t + 1]
        elif t - 1 not in d and t + 1 in d:
            head = d[t + 1]
        elif t - 1 in d and t + 1 not in d:
            d[t-1].next = None
        else:
            head = None

        return head


        
