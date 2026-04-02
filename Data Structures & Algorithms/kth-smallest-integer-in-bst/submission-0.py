# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # given it's a BST then if we traverse it in order
        # then put each element in an array then it's sorted

        # we do this iteratively using a stack

        n = 0 # number of elements
        stack = []
        cur = root

        while cur or stack: # while both are not empty
            while cur: # keep going with
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1

            # if the current value si what we're looking for
            if n == k:
                return cur.val

            # but if not
            cur = cur.right








