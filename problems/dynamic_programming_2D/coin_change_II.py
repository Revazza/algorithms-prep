from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) -1, -1, -1):
            for a in range(1, amount + 1):
                if a >= coins[i]:
                    dp[a] = dp[a] + dp[a - coins[i]]

        return dp[amount]

    '''
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]

    '''

    '''
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}

        def findWays(startIndex, total):
            if total < 0:
                return 0

            if (startIndex, total) in cache:
                return cache[(startIndex, total)]

            if total == 0:
                return 1

            ways = 0

            for i in range(startIndex, len(coins)):
                ways += findWays(i, total - coins[i])

            cache[(startIndex, total)] = ways
            return ways

        return findWays(0, amount)
    '''