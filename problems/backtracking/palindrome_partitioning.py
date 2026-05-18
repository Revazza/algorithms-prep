from typing import List


class Solution:
    def partition(self, word: str) -> List[List[str]]:

        result = []

        def collect(left, right, res: List[str]):
            if right >= len(word):
                if left == right:
                    result.append(res.copy())
                return

            if is_palindrome(left, right):
                res.append(word[left: right + 1])
                collect(right + 1, right + 1, res)
                res.pop()

            collect(left, right + 1, res)

            return

        def is_palindrome(left, right)-> bool:

            while left < right:
                if word[left] != word[right]:
                    return False
                left+=1
                right-=1

            return True

        collect(0, 0, [])
        return result


