import math
import sys
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        min_eat = sys.maxsize

        while left <= right:
            mid = (right + left) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
                if total_hours > h:
                    break

            if total_hours > h:
                left = mid + 1
            else:
                right = mid - 1
                min_eat = mid

        return min_eat
