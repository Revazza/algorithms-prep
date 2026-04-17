from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Input: temperatures = [30, 32, 33, 36, 35, 40, 28]
        #Output: [1, 4, 1, 2, 1, 0, 0]
        # stack - [32, 30,
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr = temperatures[i]

            while stack and curr > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)


        return result