class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # We solve this by computing prefix and postfix products.
        # - prefix[i] is the product of all elements to the left of index i
        # - postfix[i] is the product of all elements to the right of index i

        # Both arrays can be computed in O(n) time.

        # For prefix:
        # We traverse left -> right, where each index stores the product
        # of all elements before it.

        # For postfix:
        # We traverse right -> left, where each index stores the product
        # of all elements after it.

        # Example:
        # nums = [1, 2, 4, 6]

        # prefix  = [1, 1, 2, 8]
        # postfix = [48, 24, 6, 1]

        # Explanation:
        # prefix[0] = 1 because there are no elements to the left
        # postfix[3] = 1 because there are no elements to the right

        # To build the output:
        # output[i] = prefix[i] * postfix[i]

        # This works because prefix[i] contains the product of all elements
        # before nums[i], and postfix[i] contains the product of all elements
        # after nums[i], so nums[i] itself is excluded.

        n = len(nums)

        prefix = [1] * n
        postfix = [1] * n
        output = [1] * n

        # build prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # build postfix products
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # build output
        for i in range(n):
            output[i] = prefix[i] * postfix[i]

        return output

        # i realize now that this solution works but make 1 array each for prefix & postfix
        # but sure this is still O(n) time but takes extra O(n) space for prefix & postfix
        