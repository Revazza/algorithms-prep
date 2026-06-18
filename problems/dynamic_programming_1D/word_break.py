from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = dict()

        def doesBreak(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i]

            for w in wordDict:
                if s.startswith(w, i):
                    if doesBreak(i + len(w)):
                        return True

            cache[i] = False
            return False

        return doesBreak(0)
