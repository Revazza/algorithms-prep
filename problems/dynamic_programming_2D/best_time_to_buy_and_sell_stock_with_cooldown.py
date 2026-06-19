from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def calcMaxProfit(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in cache:
                return cache[(i, buying)]

            if buying:
                buy = calcMaxProfit(i + 1, False) - prices[i]
                skip = calcMaxProfit(i + 1, True)
                cache[(i, buying)] = max(buy, skip)
            else:
                sell = calcMaxProfit(i + 2, True) + prices[i]
                skip = calcMaxProfit(i + 1, False)
                cache[(i, buying)] = max(sell, skip)

            return cache[(i, buying)]

        return calcMaxProfit(0, True)

    '''
    def maxProfit(self, prices: List[int]) -> int:

        # Input: prices = [1, 3, 4, 0, 4]
        # Output: 6

        cache = {}

        def calcProfit(index):
            if index >= len(prices):
                return 0

            if index in cache:
                return cache[index]

            maxProfit = 0
            bought = prices[index]

            for i in range(index + 1, len(prices)):
                # Sell
                sellProfit = prices[i] - bought + calcProfit(i + 2)

                # Skip buy
                skipBuyProfit = calcProfit(i)
                maxProfit = max(maxProfit, sellProfit, skipBuyProfit)

            cache[index] = maxProfit

            return maxProfit


        return calcProfit(0)
    '''