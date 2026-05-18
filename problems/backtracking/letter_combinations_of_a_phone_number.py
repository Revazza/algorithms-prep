from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        result = []
        combination = []

        def calculate(curr):
            if curr == len(digits):
                result.append("".join(combination))
                return

            letters = get_letters(digits[curr])
            for i in range(len(letters)):
                combination.append(letters[i])
                calculate(curr + 1)
                combination.pop()

            return

        def get_letters(digit)-> str:
            letters = {
                "2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz",
            }
            return letters[digit]

        calculate(0)
        return result


