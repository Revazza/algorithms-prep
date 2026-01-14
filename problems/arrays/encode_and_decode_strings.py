from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:

        # 7#65hello2#hi6#

        # Time complexity O(n)
        # Space Complexity O(n)
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        # 7#65hello2#hi6#

        # Time complexity O(n)
        # Space Complexity O(n)
        i = 0
        result = []
        while i < len(s):
            initial_index = i;
            while s[i] != '#':
                i += 1

            size = int(s[initial_index : i])

            i += 1
            decoded = s[i: i + size]
            result.append(decoded);
            i += size;

        return result
