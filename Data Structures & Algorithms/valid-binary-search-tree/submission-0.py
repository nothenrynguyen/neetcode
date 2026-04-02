# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # right and left are boundaries
        def valid(node, left, right):
            if not node:
                return True

            # if a node doesn't match then it breaks
            if not (node.val < right and node.val > left):
                return False # node broke tree

            x = valid(node.left, left, node.val)
            y = valid(node.right, node.val, right)

            return x and y

        # default boundaries are -inf & inf 
        # since the root doesn't have boundaries
        return valid(root, float("-inf"), float("inf"))