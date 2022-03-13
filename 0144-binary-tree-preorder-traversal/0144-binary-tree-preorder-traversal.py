# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         def prTrav(root):
#             if root is None:
#                 return []


#             l, r= prTrav(root.left), prTrav(root.right)
            
#             return [a for a in [root.val, *l, *r] if a is not None]
    
#         return prTrav(root)
#         answer = []
        
#         def dfs(node):
#             if not node:
#                 return
#             # Visit root first, then the left subtree, then the right subtree.
#             answer.append(node.val)
#             dfs(node.left)
#             dfs(node.right)
        answer = []
        curr = root
        
        while curr:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree. 
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right != curr:
                    last = last.right
                    
                # If the last node is not modified, we let 
                # 'curr' be its right child. Otherwise, it means we 
                # have finished visiting the entire left subtree.
                if not last.right:
                    answer.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right
            
        return answer