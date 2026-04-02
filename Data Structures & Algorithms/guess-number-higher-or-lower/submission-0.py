# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # binary search (optimal) solution
        left = 1
        right = n

        while True:
            mid = (left + right) // 2
            result = guess(mid)

            # if the guess was too low
            if result > 0:      
                left = mid + 1

            # if the guess was too high
            elif result < 0:    
                right = mid - 1

            # we guess correctly
            else: return mid

        # time O(logn)  cuz that's just binary search
        # space O(1)    cuz we don't create anything just variables
        