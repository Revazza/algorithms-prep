class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def calc(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            ways = 0

            if s[i] == t[j]:
                ways += calc(i + 1, j + 1)

            ways += calc(i + 1, j)

            cache[(i, j)] = ways
            return ways

        return calc(0, 0)
