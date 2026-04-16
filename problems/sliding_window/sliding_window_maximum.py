from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #Input: nums = [8, 7, 6, 9], k = 2
        #Output: [8, 7, 9]

        result = []
        left = 0
        q = deque()

        for right in range(len(nums)):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                result.append(nums[q[0]])
            right += 1

        return result