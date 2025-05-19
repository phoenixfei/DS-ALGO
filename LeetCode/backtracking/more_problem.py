import collections
import heapq
from typing import List


class Solution:
    # [332. 重新安排行程](https://leetcode.cn/problems/reconstruct-itinerary/description/)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ft = collections.defaultdict(list)
        for f, t in tickets:
            ft[f].append(t)
        for t in ft.values():
            heapq.heapify(t)

        ans = []

        def dfs(start):
            arrives = ft[start]
            while arrives:
                cur = heapq.heappop(arrives)
                dfs(cur)
            ans.append(start)

        dfs("JFK")
        return ans[::-1]