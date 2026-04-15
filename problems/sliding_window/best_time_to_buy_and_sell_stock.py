from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [5,1,5,6,7,1,10]
        left = 0
        right = 0
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if prices[left] > prices[right]:
                left = right

            right = right + 1

        return max_profit