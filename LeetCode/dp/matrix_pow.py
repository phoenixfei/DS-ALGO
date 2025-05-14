from typing import List


# 矩阵乘法
def matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])
    assert n == n2
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % (10 ** 9 + 7)
    return C

# 矩阵快速幂
def matrix_pow(A: List[List[int]], p: int, F0: List[List[int]]) -> List[List[int]]:
    res = F0
    while p:
        if p & 1:
            res = matrix_mul(A, res)
        A = matrix_mul(A, A)
        p >>= 1
    return res


class Solution:
    """ 3335. 字符串转换后的长度 I
    本题通过递归实现时，会报内存不够；因此，通过递推（使用dp数组）可优化通过。
    https://leetcode.cn/problems/total-characters-in-string-after-transformations-i/
    """
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        cnt = [1] * 26
        # nxt = [0] * 26 答案不对
        for i in range(t):
            nxt = [0] * 26
            for j in range(26):
                if j == 25:
                    nxt[j] = (cnt[0] + cnt[1]) % mod
                else:
                    nxt[j] = cnt[j+1]
            cnt = nxt
        res = 0
        for ch in s:
            res = (res + cnt[ord(ch) - ord('a')]) % mod
        return res


    """ 3337. 字符串转换后的长度 II
    本题是上述第一题的变形，状态转移方程更为复杂，但其范围可控，因此需要通过 矩阵乘法+快速幂 对递推过程进行优化。
    https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/
    """
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        F0 = [[1] for _ in range(26)]
        M = [[0] * 26 for _ in range(26)]
        for i, x in enumerate(nums):
            for j in range(i + 1, i + x + 1):
                M[i][j % 26] = 1
        mat = matrix_pow(M, t, F0)
        res = 0
        for ch in s:
            res = (res + mat[ord(ch) - ord('a')][0]) % (10 ** 9 + 7)
        return res

if __name__ == '__main__':
    sl = Solution()
    s = "abcyy"
    t = 2
    print(sl.lengthAfterTransformations(s, t))