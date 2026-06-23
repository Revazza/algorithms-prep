class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

    '''
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
    '''