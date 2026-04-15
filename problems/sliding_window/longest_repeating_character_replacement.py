class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Input: "ABABCB" k = 1
        # A: 1
        # B: 1
        # A: 2

        left = 0
        right = 0
        char_count = {}
        max_window = k

        while right < len(s):
            if s[right] not in char_count:
                char_count[s[right]] = 1
            else:
                char_count[s[right]] = char_count[s[right]] + 1

            while True:
                window = right - left + 1
                max_common = max(char_count.values())
                if window - max_common <= k:
                    max_window = max(window, max_window)
                    break
                char_count[s[left]] = char_count[s[left]] - 1
                left = left + 1

            right = right + 1

        return max_window
