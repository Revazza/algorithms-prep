import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        cache = dict()

        def count_coins(total):
            if total < 0:
                return sys.maxsize

            if total == 0:
                return 0

            if total in cache:
                return cache[total]

            min_coins = sys.maxsize

            for i in range(len(coins) - 1, -1, -1):

                count = count_coins(total - coins[i])
                if count == sys.maxsize:
                    continue

                min_coins = min(count + 1, min_coins)

            cache[total] = min_coins
            return cache[total]

        res = count_coins(amount)
        if res == sys.maxsize:
            return -1

        return res
