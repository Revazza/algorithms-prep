import heapq
from collections import deque
from typing import List, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","C","A","B","D","B"] n = 1

        heap = [-v for v in Counter(tasks).values()]
        heapq.heapify(heap)
        queue = deque([])
        time = 0

        while heap or queue:
            curr = 0
            if heap:
                curr = heapq.heappop(heap)
                curr += 1

            time += 1

            if curr != 0:
                cooldown = time + n
                queue.append((curr, cooldown))

            while queue and queue[0][1] <= time:
                val, _ = queue.popleft()
                heapq.heappush(heap, val)

        return time
