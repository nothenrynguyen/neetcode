class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:  # while stack is not empty and height of top val in stack > 1
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))    # width = current index i - start index which we just popped
                start = index   # we can extend our index backwards
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        # O(n) time and space cuz we iterate thru array once and create a stack/list