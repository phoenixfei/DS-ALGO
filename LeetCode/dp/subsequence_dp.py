from typing import List


class Solution:
    """ 2901. 最长相邻不相等子序列 II
    https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-ii/description/
    """
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamming_check(s1: str, s2: str) -> bool:
            return len(s1) == len(s2) and (sum([a != b for a, b in zip(s1, s2)]) == 1)

        n = len(words)
        dp = [1] * n
        idx = [-1] * n
        max_idx = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if dp[j] + 1 > dp[i] and groups[i] != groups[j] and hamming_check(words[i], words[j]):
                    dp[i] = dp[j] + 1
                    idx[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i
        ans = []
        while max_idx != -1:
            ans.append(words[max_idx])
            max_idx = idx[max_idx]
        return ans
