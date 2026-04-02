class Solution:
    def climbStairs(self, n: int) -> int:

        # my intuition would do the recursive solution
        # but its O(n^2) which times out here

        # so this is the optimal top-down dynamic programming approach

        cache = [-1] * n

        def DFS(step):
            if step >= n:
                return step == n
            
            if cache[step] != -1:
                return cache[step]
            cache[step] = DFS(step + 1) + DFS(step + 2)

            return cache[step]

        return DFS(0)