# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # base if both empty then equal
        if not p and not q:
            return True

        # bases if 1 is empty then not equal
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # recurive step
        x = self.isSameTree(p.left, q.left)
        y = self.isSameTree(p.right, q.right)

        # return if the lefts are equal AND rights are equal
        return x and y