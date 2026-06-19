class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # abc
        # astonmartin
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}

        def find(smallText, largeText):
            if len(smallText) == 0:
                return 0

            if smallText in cache:
                return cache[smallText]

            if isSub(smallText, largeText):
                return len(smallText)

            longest = 0

            for i in range(len(smallText)):
                longest = max(longest, find(smallText[:i] + smallText[i + 1:], largeText))

            cache[smallText] = longest
            return longest

        def isSub(word1, word2):
            i = 0
            k = 0

            while i < len(word1) and k < len(word2):
                if word1[i] == word2[k]:
                    i += 1
                k += 1

            return i == len(word1)

        if len(text1) > len(text2):
            return find(text2, text1)

        return find(text1, text2)
    '''
