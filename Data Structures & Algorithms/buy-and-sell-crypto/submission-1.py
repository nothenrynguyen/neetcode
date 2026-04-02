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
                left = right # if right < left then we have a new min buy
            right += 1

        return maxPrice