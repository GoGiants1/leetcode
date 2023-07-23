# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def dp(cnt: int)->list[TreeNode]:
            out = []
            if cnt == 0:
                return out
            if cnt == 1:
                out.append(TreeNode())
                return out
            for i in range(cnt - 1):
                l = dp(i)
                r = dp(cnt - 1 - i)
                if len(l) == 0 or len(r) == 0:
                    continue
                for left in l:
                    for right in r:
                        rt = TreeNode()
                        rt.left = left
                        rt.right = right
                        out.append(rt)
            return out
        
        return dp(n)
                        
