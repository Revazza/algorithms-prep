import sys
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        #s = "ADOBECODEBANC"
        #t = "ABC
        #OUTPUT: "BANC"

        t_count = Counter(t)
        window = Counter("")
        need = len(t_count)
        min_length = sys.maxsize
        min_left = 0
        have = 0
        left = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:
                if min_length > right - left + 1:
                    min_left = left
                    min_length = right - left + 1

                left_char = s[left]
                window[left_char] -= 1
                if char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1
                left += 1

        if min_length == sys.maxsize:
            return ""

        return s[min_left: min_left + min_length]
