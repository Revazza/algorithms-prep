import sys
from typing import List


class Solution:
    # Not correct solution
    def oddEvenJumps(self, arr: List[int]) -> int:

        # [2,3,1,1,4]
        dp = [False] * len(arr)
        dp[-1] = True
        count = 0
        currMin = sys.maxsize
        currMax = -sys.maxsize

        for i in range(len(arr) - 2, -1, -1):

            currMin = min(currMin, arr[i + 1])

            if arr[i] <= arr[i + 1] and arr[i + 1] == currMin and dp[i + 1]:
                dp[i] = True
                count += 1
                continue

            currMax = max(arr[i + 2], currMax)

            if arr[i] >= arr[i + 2] and arr[i + 2] == currMax and dp[i + 2]:
                dp[i] = True
                count += 1

        return count

