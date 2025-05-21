from itertools import accumulate
from typing import List


class Solution:
    # [3355. 零数组变换 I](https://leetcode.cn/problems/zero-array-transformation-i/description/)
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums)+1)
        for i, j in queries:
            diff[i] += 1
            diff[j+1] -= 1
        for d, x in zip(nums, accumulate(diff)):
            if d > x:
                return False
        return True

    # [3356. 零数组变换 II](https://leetcode.cn/problems/zero-array-transformation-ii/description/)
    # 利用开区间进行二分查找
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def check(k) -> bool:
            diff = [0] * (n + 1)
            for l, r, v in queries[:k]:
                diff[l] += v
                diff[r + 1] -= v
            for d, sum_d in zip(nums, accumulate(diff)):
                if d > sum_d:
                    return False
            return True

        q = len(queries)
        left, right = -1, q + 1  # 题目问的是选取元素的个数
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if right <= q else -1

