class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        buy=float("inf")
        for i in range(0,len(prices)):
            buy=min(buy,prices[i])
            profit=prices[i]-buy
            max_profit=max(profit,max_profit)
        return max(max_profit,0)
        