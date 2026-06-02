from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]

        def find(x):
            while x != par[x]:
                x = par[x]
            return par[x]

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            par[p2] = p1
            return True

        for n1,n2 in edges:
            if union(n1,n2):
                n -= 1

        return n
