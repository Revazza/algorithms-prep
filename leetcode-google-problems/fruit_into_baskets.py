import sys
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l = 0
        r = 0
        maxPicked = -sys.maxsize
        picked = dict()

        for r in range(len(fruits)):
            picked[fruits[r]] = picked.get(fruits[r], 0) + 1

            while l < r and len(picked) > 2:
                picked[fruits[l]] -= 1

                if picked[fruits[l]] == 0:
                    del picked[fruits[l]]

                l += 1

            maxPicked = max(maxPicked, r - l + 1)

        return maxPicked




