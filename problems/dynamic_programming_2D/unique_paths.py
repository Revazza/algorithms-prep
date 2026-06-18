class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        dp = {(m - 1, n - 1): 1}

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row + 1 == m or col + 1 == n:
                    dp[(row, col)] = 1
                else:
                    dp[(row, col)] = dp[(row + 1, col)] + dp[(row, col + 1)]

        return dp[(0, 0)]

    '''
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}
        def calc(row, col):
            if row < 0 or col < 0 or row == m or col == n:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in cache:
                return cache[(row, col)]

            ways = calc(row + 1, col) + calc(row, col + 1)

            cache[(row, col)] = ways

            return cache[(row, col)]

        return calc(0, 0)
'''
