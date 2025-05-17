from typing import List


class Solution:
    # [131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/)
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []
        def dfs(start_index):
            if start_index == n:
                ans.append(path.copy())
                return
            for i in range(start_index, n):
                if s[start_index:i+1] == s[start_index:i+1][::-1]:
                    path.append(s[start_index:i+1])
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return ans

    # [93. 复原IP地址](https://leetcode.cn/problems/restore-ip-addresses/description/)
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(ip: str) -> bool:
            if len(ip) > 1 and ip[0] == '0':
                return False
            return 0 <= int(ip) <= 255

        n = len(s)
        ans = []
        path = []
        def dfs(start_index):
            c = len(path)
            # 超过4个整数，或者剩余的字符 比 剩余的整数都按最大个数统计 都要多的时候，剪枝
            if n - start_index > 3 * (4 - c):
                return
            if start_index == n and c == 4:
                ans.append('.'.join(path))
                return
            for i in range(start_index, min(n, start_index+3)):
                if check(s[start_index:i+1]):
                    path.append(s[start_index:i+1])
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return ans

if __name__ == '__main__':
    sl = Solution()
    print(sl.restoreIpAddresses("25525511135"))
