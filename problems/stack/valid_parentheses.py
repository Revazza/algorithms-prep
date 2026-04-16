from inspect import stack


class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        left = 0
        stack = []

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False;
                c = stack.pop()
                if pairs[c] != char:
                    return False;

        return len(stack) == 0
