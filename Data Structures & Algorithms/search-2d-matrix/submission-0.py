class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0             # top row
        bot = rows - 1      # bottom row

        # binary search on the rows
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bot = row - 1

            else:   # meaning the target val is witin that row
                break

        if not (top <= bot):    # if none of the rows contain the target val
            return False

        # binary search within the current row

        row = (top + bot) // 2
        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[row][mid]:
                left = mid + 1

            elif target < matrix[row][mid]:
                right = mid - 1

            else:
                return True

        return False