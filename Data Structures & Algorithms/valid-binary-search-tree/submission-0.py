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

        def valid_max(root, left_sub):
            if not left_sub.right:
                return root.val>left_sub.val
            return valid_max(root, left_sub.right)
        def valid_min(root, right_sub):
            if not right_sub.left:
                return root.val<right_sub.val
            return valid_min(root, right_sub.left)

        if root.left:
            if not valid_max(root, root.left):
                return False
            if not self.isValidBST(root.left):
                return False
        if root.right:
            if not valid_min(root, root.right):
                return False
            if not self.isValidBST(root.right):
                return False
        if root.left and root.right:
            if not root.left.val<root.val<root.right.val:
                return False
        return True
        