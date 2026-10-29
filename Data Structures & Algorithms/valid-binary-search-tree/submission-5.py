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
            if root.left:
                dfs(root.left)
            travel.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        for i in range(len(travel)-1):
            if travel[i+1]<=travel[i]:
                return False
        return True

        