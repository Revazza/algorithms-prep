class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = dict()

        def find_longest(left, right):
            if is_palindrome(left, right):
                return s[left:right + 1]

            if (left, right) in dp:
                return dp[(left, right)]

            left_sub = find_longest(left + 1, right)
            right_sub = find_longest(left, right - 1)

            if len(left_sub) >= len(right_sub):
                dp[(left, right)] = left_sub
                return left_sub

            dp[(left, right)] = right_sub
            return right_sub

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        return find_longest(0, len(s) - 1)
