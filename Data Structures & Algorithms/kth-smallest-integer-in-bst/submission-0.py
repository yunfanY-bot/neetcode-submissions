# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def in_order_dfs(node):
            if not node:
                return
            in_order_dfs(node.left)
            in_order.append(node.val)
            in_order_dfs(node.right)
        in_order_dfs(root)

        return in_order[k-1]
        