class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        uniques = set()

        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            if s[right] not in uniques:
                uniques.add(s[right])
                right = right + 1
            else:
                max_length = max(len(uniques), max_length)
                while s[right] in uniques:
                    uniques.remove(s[left])
                    left = left + 1

        return max(max_length, len(uniques))