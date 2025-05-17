from typing import List


class Solution:
    # [78. 子集](https://leetcode.cn/problems/subsets/description/)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(start_index):
            ans.append(path.copy())
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans


    # [90. 子集 II](https://leetcode.cn/problems/subsets-ii/description/)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        def dfs(start_index):
            ans.append(path.copy())
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans


    # https://leetcode.cn/problems/non-decreasing-subsequences/description/
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(start_index):
            if len(path) >= 2:
                ans.append(path.copy())
                # 注意这里不要加return，因为要取树上的所有节点
            used = set()
            for i in range(start_index, len(nums)):
                if path and nums[i] < path[-1]:
                    continue
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans


