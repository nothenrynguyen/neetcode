class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # this solution is a monotonic stack / monotonic decreasing stack

        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:       # [-1] is top of stack and [0] is temp which is first val in that pair
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append([t, i])

        return result       # we don't need to fill in the extra 0s cuz we initialize it default at the start
