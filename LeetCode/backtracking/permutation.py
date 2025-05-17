from typing import List


class Solution:
    # [46. 全排列](https://leetcode.cn/problems/permutations/description/)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                used[i] = False
                path.pop()
        dfs()
        return ans


    # [47. 全排列 II](https://leetcode.cn/problems/permutations-ii/description/)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                path.pop()
        dfs()
        return ans

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            cur_used = set()
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                if nums[i] in cur_used:
                    continue
                cur_used.add(nums[i])
                path.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                path.pop()
        dfs()
        return ans