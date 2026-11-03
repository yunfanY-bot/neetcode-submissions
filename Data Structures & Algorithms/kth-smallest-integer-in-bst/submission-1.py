# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = 0

        def in_order_dfs(node):
            nonlocal res, count
            if not node:
                return
            in_order_dfs(node.left)
            count += 1
            if count == k:
                res  = node.val
                return
            
            
            in_order_dfs(node.right)


        in_order_dfs(root)

        return res
        