# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = {}

        def dfs(rt: TreeNode, lv: int):
            if rt is None:
                return
            if lv in d:
                d[lv][0] += rt.val
                d[lv][1] += 1
            else:
                d[lv] = [rt.val, 1]

            if rt.left:
                dfs(rt.left, lv + 1)
            if rt.right:
                dfs(rt.right, lv + 1)
        
        dfs(root, 0)
        out = []
        for k, v in d.items():
            while len(out) <= k:
                out.append(0)
            out[k] = v[0] / v[1]
        return out