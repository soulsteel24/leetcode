class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        n = len(prices)
        min_price = float("inf")
        for i in range(0,n):
            min_price = min(prices[i],min_price)
            maxp = max(maxp, prices[i]-min_price)
        return maxp