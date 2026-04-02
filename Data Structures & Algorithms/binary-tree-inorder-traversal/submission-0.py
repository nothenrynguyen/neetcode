# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # recursive solution

        result = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)          # first go thru left subtree
            result.append(root.val)     # then process root node itself
            inorder(root.right)

        inorder(root)

        return result
        