# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        # depth
        target_depth = 0
        t_node = None
        # find target node
        q = deque()
        q.append((root, 0))
        while q:
            node, depth = q.popleft()
            if node.val == target.val:
                target_depth = depth
                t_node = node
                break

            if node.left:
                q.append((node.left, depth + 1))
                parent[node.left.val] = node
            if node.right:
                q.append((node.right, depth + 1))
                parent[node.right.val] = node
        # from target node, do bfs
        q.clear()
        visit = {target.val}
        q.append((t_node, 0))
        out = []
        while q:
            node, dist = q.popleft()
            if dist == k:
                out.append(node.val)
            elif dist > k:
                continue
            neighbors = [node.left, node.right] if node.val not in parent else [node.left, node.right, parent[node.val]]
            for nd in neighbors:
                if nd and nd.val not in visit:
                    q.append((nd, dist + 1))
                    visit.add(nd.val)
        return out
