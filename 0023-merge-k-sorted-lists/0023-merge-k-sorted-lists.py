# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge! sorted linked list
        if len(lists) < 2:
            if len(lists) == 0:
                return None
            return lists[0]
        
        
        # heapq 이용해서 min heap?
        # (self.val, Node)
        
        # heappush(hq, ())
        
        
        hm = defaultdict(list)
        vals = set()
        lists = [l for l in lists if l is not None]
        
        while lists:
            for i, v in enumerate(lists):
                vals.add(v.val)
                hm[v.val].append(v)
                v = v.next
                lists[i] = v
            
            lists = [l for l in lists if l is not None]
            
        sorted_vals = sorted(vals)
        head = curr = None
        
        for v in sorted_vals:
            for node in hm[v]:
                if head is None:
                    head, curr = node, node
                    continue
                
                curr.next = node
                curr = node

                
                
        
        
        return head
        