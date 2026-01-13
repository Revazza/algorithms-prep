from collections import Counter, defaultdict
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #   Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    #   Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

    anagrams = {};

    for s in strs:
        key = tuple(sorted(s));
        if key in anagrams:
            anagrams[key].append(s);
            continue;

        anagrams[key] = [s];

    return list(anagrams.values());

def groupAnagramsFaster(self, strs: List[str]) -> List[List[str]]:
    #   Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    #   Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

    anagrams = defaultdict(list)

    for s in strs:
        count = [0] * 26;
        for ch in s:
            count[ord(ch) - ord('a')] += 1;
        key = tuple(count);
        anagrams[key].append(s);

    return list(anagrams.values());