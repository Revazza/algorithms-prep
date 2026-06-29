import heapq
from collections import deque
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # Input: hand = [1, 2, 4, 2, 3, 5, 3, 4], groupSize = 4
        # Output: true
        # Explanation: The cards can be rearranged as [1, 2, 3, 4] and [2, 3, 4, 5].

        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1

        minHp = list(count.keys())
        heapq.heapify(minHp)

        while minHp:
            first = minHp[0]

            for n in range(first, first + groupSize):
                if n not in count:
                    return False

                count[n] -= 1
                if count[n] == 0:
                    if n != minHp[0]:
                        return False
                    heapq.heappop(minHp)

        return True
