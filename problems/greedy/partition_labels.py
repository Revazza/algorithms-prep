from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        mapping = {}

        # xyxxyzbzbbisl
        # x - 3
        # y - 4
        # z - 7
        # b - 9
        # i - 10
        # s - 11
        # l - 12

        for i, c in enumerate(s):
            mapping[c] = i

        result = []
        lastIndex = 0
        count = 0
        for i in range(len(s)):
            char = s[i]
            lastIndex = max(lastIndex, mapping[char])
            count += 1
            if lastIndex == i:
                result.append(count)
                count = 0

        return result
