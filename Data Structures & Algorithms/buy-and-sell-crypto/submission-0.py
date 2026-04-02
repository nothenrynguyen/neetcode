class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 # buying
        right = 1 # selling

        maxPrice = 0

        while right < len(prices):

            # profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxPrice = max(maxPrice, profit)
            else: 
                left = right
            right += 1

        return maxPrice