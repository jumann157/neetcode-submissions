class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        pointer_a = 0
        pointer_b = 1
        max_profit = 0 
        
        while pointer_b < len(prices):
            if prices[pointer_b] > prices[pointer_a]:
                profit = prices[pointer_b] - prices[pointer_a]
                max_profit = max(max_profit, profit)
            else:
                pointer_a = pointer_b
            pointer_b += 1
        
        return max_profit