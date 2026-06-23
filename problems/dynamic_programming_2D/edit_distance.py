import sys


class Solution:
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
