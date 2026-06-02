import sys
from collections import deque
from typing import List, Counter, reveal_type


class Solution:
    def ladderLength(self, begin_word: str, target: str, word_list: List[str]) -> int:
        visited = set()

        def is_applicable(word1, word2):
            differences = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    differences += 1
                if differences > 1:
                    return False

            return differences == 1

        queue = deque([(begin_word, 1)])
        picked = set()

        while queue:
            word, steps = queue.popleft()

            if word == target:
                return steps

            picked.add(word)

            for w in word_list:
                if w in picked or not is_applicable(word, w):
                    continue
                queue.append((w, steps + 1))

        return 0

