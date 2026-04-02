# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # root node is a good node 

        def dfs(node, maxVal):
            if not node:
                return 0

            # +1 to result if the node is good 
            result = 1 if node.val >= maxVal else 0

            # keep tracking the max node in path
            maxVal = max(maxVal, node.val)

            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            return result
        
        return dfs(root, root.val)