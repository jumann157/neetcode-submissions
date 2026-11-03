class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        maxProfit = 0

        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
            else:
                profit = prices[p2] - prices[p1]
                if profit > maxProfit:
                    maxProfit = profit
            p2 += 1

        return maxProfit





