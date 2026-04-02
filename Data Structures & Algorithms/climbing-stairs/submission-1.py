class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n

        def DFS(step):
            if step >= n:
                return step == n
            
            if cache[step] != -1:
                return cache[step]
            cache[step] = DFS(step + 1) + DFS(step + 2)

            return cache[step]

        return DFS(0)