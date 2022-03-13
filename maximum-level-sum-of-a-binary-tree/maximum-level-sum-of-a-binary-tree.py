# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # BFS

        # q = deque()
        # q.append((root, 1))
        # d = defaultdict(int)
        # while q:
        #     node, lv = q.popleft()
        #     if node:
        #         d[lv] += node.val
        #         q.append((node.left, lv + 1))
        #         q.append((node.right, lv + 1))
        
        # m = -math.inf
        # for k, v in d.items():
        #     m = max(m, v)
        # for k, v in d.items():
        #     if v == m:
        #         return k
        max_sum, ans, level = float('-inf'), 0, 0

        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            sum_at_current_level = 0
            # Iterate over all the nodes in the current level.
            for _ in range(len(q)):
                node = q.popleft()
                sum_at_current_level += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < sum_at_current_level:
                max_sum, ans = sum_at_current_level, level
        return ans
           