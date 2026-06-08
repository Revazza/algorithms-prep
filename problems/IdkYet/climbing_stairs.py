class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[-1] = 1
        dp[-2] = 1

        n -= 2

        while n >= 0:
            dp[n] = dp[n + 1] + dp[n + 2]
            n -= 1

        return dp[0]
