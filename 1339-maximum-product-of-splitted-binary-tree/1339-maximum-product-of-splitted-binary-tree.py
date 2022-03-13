# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
#         from collections import deque
#         max_int = 10 ** 9 + 7
#         # BFS
        
#         dq = deque(root)
#         visited = []
#         while len(dq) > 0:
#             visit = dq.popleft()
#             visited.append(visit.val if visit is not None else 0)
            
#             dq.append(visit.left)
#             dq.append(visit.right)
        
#         return ans % max_int
        sub_tree_sums = []
        def tree_sum(sub_root: Union[TreeNode | None]):
            if sub_root is None:
                return 0
            l, r = tree_sum(sub_root.left), tree_sum(sub_root.right)
            tmp = sub_root.val + l + r
        
            sub_tree_sums.append(tmp)
            return tmp
        
        total = tree_sum(root)
        best_product = 0
        for i in sub_tree_sums:
            new_product = i * (total -i)
            if best_product < new_product:
                best_product = new_product
        return best_product % (10 ** 9 + 7)
    
    