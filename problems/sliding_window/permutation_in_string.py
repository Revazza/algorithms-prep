from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Input: s1 = "abc", s2 = "lecaabee"

        if len(s1) > len(s2):
            return False

        window = Counter(s2[0:len(s1)])
        s1_count = Counter(s1)

        if s1_count == window:
            return True

        for i in range(len(s1), len(s2)):

            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1

            if s1_count == window:
                return True

        return False
