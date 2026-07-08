class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        cheap = prices[0]

        for i in range(1,n):

            profit = prices[i] - cheap
            maxProfit = max(maxProfit,profit)
            cheap = min(cheap,prices[i])

        return maxProfit