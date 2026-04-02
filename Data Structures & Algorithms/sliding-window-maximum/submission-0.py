class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) 

            # remove left val from windows
            if l > q[0]:
                q.popleft()

            # edge case
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1  # left only increments when window is at least size k
            r += 1      # right always increments

        return output