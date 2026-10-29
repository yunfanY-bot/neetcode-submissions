# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        travel = []

        def dfs(root):
            if not root:
                return True
            if root.left:
                if not dfs(root.left):
                    return False
            if travel and root.val<=travel[-1]:
                return False
            travel.append(root.val)
            if root.right:
                if not dfs(root.right):
                    return False
            return True
        return dfs(root)
        