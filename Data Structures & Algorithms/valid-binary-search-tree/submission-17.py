# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isvalid(root, -1*float('inf'), float('inf'))

    def isvalid(self, root, left, right):

        if not root:
            return True
        return left<root.val<right and self.isvalid(root.left, left, root.val) and self.isvalid(root.right, root.val, right)        