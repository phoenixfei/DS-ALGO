from typing import List


class Solution:

    # [77. 组合](https://leetcode.cn/problems/combinations/description/)
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(start_index):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(start_index, n+1-(k-len(path))+1):
                path.append(i)
                dfs(i+1)
                path.pop()
        dfs(1)
        return ans


    # [216. 组合总和 III](https://leetcode.cn/problems/combination-sum-iii/description/)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(start_index, left_val):
            if left_val < 0:
                return
            if len(path) == k and left_val == 0:
                ans.append(path.copy())
                return
            for i in range(start_index, 10 - (k - len(path)) + 1):
                path.append(i)
                dfs(i+1, left_val-i)
                path.pop()
        dfs(1, n)
        return ans


    # [17.电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        call = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        path = []
        def dfs(depth):
            if depth == len(digits):
                ans.append("".join(path))
                return
            for x in call[int(digits[depth])]:
                path.append(x)
                dfs(depth+1)
                path.pop()
        dfs(0)
        return ans


    # [39. 组合总和](https://leetcode.cn/problems/combination-sum/description/)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(start_index, left_val):
            if left_val < 0:
                return
            if left_val == 0:
                ans.append(path.copy())
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                dfs(i, left_val-candidates[i])
                path.pop()
        dfs(0, target)
        return ans


    # [216. 组合总和 II](https://leetcode.cn/problems/combination-sum-ii/description/)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def dfs(start_index, left_val):
            if left_val < 0:
                return
            if left_val == 0:
                ans.append(path.copy())
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, left_val-candidates[i])
                path.pop()
        dfs(0, target)
        return ans

    # 使用used数组对元素进行去重
    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        used = [False] * len(candidates)
        def dfs(start_index, left_val):
            if left_val < 0:
                return
            if left_val == 0:
                ans.append(path.copy())
            for i in range(start_index, len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1] and used[i-1] == False:
                    continue
                used[i] = True
                path.append(candidates[i])
                dfs(i+1, left_val-candidates[i])
                used[i] = False
                path.pop()
        dfs(0, target)
        return ans

    def combinationSum2_3(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        ans = []
        path = []
        def dfs(start_index, left_val):
            if left_val < 0:
                return
            if left_val == 0:
                ans.append(path.copy())
            used = set()
            for i in range(start_index, len(candidates)):
                if candidates[i] in used:
                    continue
                used.add(candidates[i])
                path.append(candidates[i])
                dfs(i+1, left_val-candidates[i])
                path.pop()
        dfs(0, target)
        return ans