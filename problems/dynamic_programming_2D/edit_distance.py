import sys


class Solution:

    def minDistance(self, word: str, target: str) -> int:

       m = len(word)
       n = len(target)
       dp = [[0] * (n + 1) for _ in range(m + 1)]

       for i in range(m + 1):
           dp[i][n] = m - i
       for i in range(n + 1):
           dp[m][i] = n - i

       for i in range(m - 1, - 1, -1):
           for j in range(n - 1, - 1, -1):
               if word[i] == target[j]:
                   dp[i][j] = dp[i + 1][j + 1]
               else:
                   removeWays = 1 + dp[i + 1][j]
                   replaceWays = 1 + dp[i + 1][j + 1]
                   insertWays = 1 + dp[i][j + 1]
                   dp[i][j] = min(removeWays, replaceWays, insertWays)

       return dp[0][0]

    '''
    def minDistance(self, word: str, target: str) -> int:

        cache = {}

        def calc(i, j):

            if i == len(word):
                return len(target) - j

            if j == len(target):
                return len(word) - i

            if (i, j) in cache:
                return cache[(i, j)]

            if word[i] == target[j]:
                minDistance = calc(i + 1, j + 1)
            else:
                removeWays = 1 + calc(i + 1, j)
                replaceWays = 1 + calc(i + 1, j + 1)
                insertWays = 1 + calc(i, j + 1)
                minDistance = min(removeWays, replaceWays, insertWays)

            cache[(i, j)] = minDistance
            return cache[(i, j)]

        return calc(0, 0)
    '''