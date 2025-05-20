from collections import deque
from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    # 双指针
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                nums[a], nums[i] = nums[i], nums[a]
                if a < b:
                    nums[b], nums[i] = nums[i], nums[b]
                a += 1
                b += 1
            elif nums[i] == 1:
                nums[b], nums[i] = nums[i], nums[b]
                b += 1
            i += 1


    ''' 动态规划
        # [1931. 用三种不同颜色为网格涂色](https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/)
        for d in vld:
        for i in range(m):
            print(d // (3 ** i) % 3, end=" ")
        print()
    '''
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 全局的变量都要提前预处理，不要放到for循环中计算
        vld = []
        for d in range(3**m):
            if all([d//(3**i)%3 != d//(3**(i+1))%3 for i in range(m-1)]):
                vld.append(d)
        K = len(vld) # x个元素
        nv = [[] for _ in range(K)]
        for p, k in enumerate(vld):
            for q, v in enumerate(vld):
                if all([v // (3 ** i) % 3 != k // (3 ** i) % 3 for i in range(m)]):
                    nv[p].append(q)
        pre = [1] * K
        for _ in range(1, n):
            nxt = [0] * K
            for p, k in enumerate(vld):
                for q in nv[p]:
                    nxt[p] += (pre[q]) % MOD
            pre = nxt
        return sum(pre) % MOD


    def colorTheGrid2(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        vld = []
        for d in range(3**m):
            if all([d//(3**i)%3 != d//(3**(i+1))%3 for i in range(m-1)]):
                vld.append(d)
        K = len(vld)  # x个元素
        nv = [[] for _ in range(K)]
        for p, k in enumerate(vld):
            for q, v in enumerate(vld):
                if all([v // (3 ** i) % 3 != k // (3 ** i) % 3 for i in range(m)]):
                    nv[p].append(q)

        @cache
        def dfs(n, k):
            if n == 0:
                return 1
            ans = 0
            for v in nv[k]:
                ans += dfs(n-1, v) % MOD
            return ans % MOD
        ans = 0
        for k in range(K):
            ans += dfs(n-1, k) % MOD
        return ans % MOD


    def minSwaps(self, nums: List[int]) -> int:
        def sort_key(x):
            v = 0
            while x > 0:
                v += (x % 10)
                x //= 10
            print(v)
            return v

        sort_nums = sorted(nums, key=lambda item: (sort_key(item), item))
        index_map = {}
        for i, x in enumerate(nums):
            index_map[x] = i

        ans =0
        for i in range(len(nums)):
            while sort_nums[i] != nums[i]:
                ans += 1
                new_index = index_map[sort_nums[i]]
                sort_nums[i], sort_nums[new_index] = sort_nums[new_index], sort_nums[i]
        return ans

    # djst/0-1bfs（不用vst）
    def minMoves(self, matrix: List[str]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dis = [[float('inf')] * n for _ in range(m)]
        # trans = [[] * 26]
        trans = [[] for _ in range(26)]
        for i in range(m):
            for j in range(n):
                idx = ord(matrix[i][j]) - ord('A')
                if 0 <= idx < 26:
                    trans[idx].append((i, j))

        dq = deque()
        dq.append((0, 0))
        dis[0][0] = 0
        while dq:
            x, y = dq.popleft()
            if x == m - 1 and y == n - 1:
                return int(dis[x][y])
            idx = ord(matrix[x][y]) - ord('A')
            if 0 <= idx < 26:
                can_tran = trans[idx]
                for i, j in can_tran:
                    if dis[x][y] < dis[i][j]:
                        dis[i][j] = dis[x][y]
                        dq.appendleft((i, j))
                trans[idx] = []

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != '#' and dis[x][y] + 1 < dis[i][j]:
                    dis[i][j] = dis[x][y] + 1
                    dq.append((i, j))
        return -1

    # https://leetcode.cn/problems/zero-array-transformation-i/description/
    # 差分数组
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums)+1)
        for i, j in queries:
            diff[i] += 1
            diff[j+1] -= 1
        for d, x in zip(nums, accumulate(diff)):
            if d > x:
                return False
        return True


if __name__ == '__main__':
    sl = Solution()
    # nums = [346675656,436516098,372126778,781771807]
    # sl.minSwaps(nums)
    print(sl.colorTheGrid(m=5, n=5))