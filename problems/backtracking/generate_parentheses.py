from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        combination = []

        def gather(opened, closed):
            if opened == n and closed == n:
                result.append("".join(map(str, combination)))
                return

            if opened < n:
                combination.append("(")
                gather(opened + 1, closed)
                combination.pop()

            if closed < opened:
                combination.append(")")
                gather(opened, closed + 1)
                combination.pop()

        gather(0, 0)

        return result