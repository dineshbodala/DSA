class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -1
        max_profit = -9999
        buying_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < buying_price:
                buying_price = prices[i]
            else:
                profit = prices[i] - buying_price
                max_profit = max(profit, max_profit)
        
        return max(0, max_profit)