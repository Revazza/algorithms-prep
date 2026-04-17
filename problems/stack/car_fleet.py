from typing import List
from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        stack = []

        for ps, spd in pairs:
            stack.append((target - ps) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
