class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        cheapest = prices[0]

        for i in range(n):
            if prices[i] < cheapest:
                cheapest = prices[i]

            profit = prices[i] - cheapest
            maxProfit = max(maxProfit,profit)

        return maxProfit