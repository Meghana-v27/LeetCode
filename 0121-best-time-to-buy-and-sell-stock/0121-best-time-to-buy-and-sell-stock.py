class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        max_price=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            profit=max_price-prices[i]
            if profit>max_profit:
                max_profit=profit
            if prices[i]>max_price:
                max_price=prices[i]
        return max_profit
        