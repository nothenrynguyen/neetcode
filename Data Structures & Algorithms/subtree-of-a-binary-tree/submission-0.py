# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # if the t tree is empty then it is a subtree
        if not subRoot: return True

        # if s main tree is empty but t is not
        if not root: return False

        if self.sameTree(root, subRoot):
            return True 

        # if t is the same as the left or right subtree of s
        x = self.isSubtree(root.left, subRoot)
        y = self.isSubtree(root.right, subRoot)

        return x or y
    
    
    def sameTree(self, s, t):
        # if both are empty then they are the same
        if not s and not t:
            return True
        
        # if neither are empty and their val are same
        if s and t and s.val == t.val:
            # then compare left and right subtree
            # x returns True if s.left == t.left
            # y returns True if s.right == t.right
            x = self.sameTree(s.left, t.left)
            y = self.sameTree(s.right, t.right)

            # function returns True if both are True
            return x and y

        # if one of the trees is empty and the other is non-empty
        return False

        