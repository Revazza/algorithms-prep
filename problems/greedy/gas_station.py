from typing import List

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1,2,3,4], cost = [2,2,4,1]

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start

    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # gas = [1,2,3,4], cost = [2,2,4,1]
        # tank = 3
        # tank =
        start = len(gas) - 1
        end = 0
        tank = gas[start] - cost[start]

        while start > end:

            if tank >= 0:
                tank += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                tank += gas[start] - cost[start]

        return start if tank >= 0 else -1
    '''

    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # gas = [1,2,3,4], cost = [2,2,4,1]

        for start in range(0, len(gas)):
            i = start + 1
            curr = gas[start]
            while True:
                if i == len(gas):
                    i = 0

                if i == start:
                    return i

                if curr - cost[i] < 0:
                    break

                curr += gas[i]
                curr -= cost[i]
                i += 1

        return -1
    '''