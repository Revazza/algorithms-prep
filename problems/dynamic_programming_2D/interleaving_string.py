class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1 ,-1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

        # aabc
        cache = {}

        def ok(i, j):
            k = i + j
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j) in cache:
                return cache[(i, j)]

            answer = False

            if i < len(s1) and s1[i] == s3[k]:
                answer |= ok(i + 1, j)
            if j < len(s2) and s2[j] == s3[k]:
                answer |=  ok(i, j + 1)

            cache[(i, j)] = answer

            return cache[(i, j)]

        return ok(0, 0)
    '''