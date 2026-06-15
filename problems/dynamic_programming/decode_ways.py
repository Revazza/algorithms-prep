class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {str(i + 1): chr(ord('A') + i) for i in range(26)}
        cache = dict()

        def count_decoding_top_down(i):
            if i >= len(s):
                return 1

            if s[i] not in mapping:
                return 0

            if i in cache:
                return cache[i]

            count = count_decoding_top_down(i + 1)

            if (i + 1) < len(s) and s[i:i+2] in mapping:
                count += count_decoding_top_down(i + 2)

            cache[i] = count
            return count

        return count_decoding_top_down(0)
