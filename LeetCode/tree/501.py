# 二叉搜索树具有如下特征：
# * 节点的左子树只包含小于当前节点的数。
# * 节点的右子树只包含大于当前节点的数。
# * 所有左子树和右子树自身必须也是二叉搜索树。
from math import inf
# **利用二叉搜索树特性，遍历求解节点间关系的相关问题**
# * [501. 二叉搜索树中的众数](https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/)
# * [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/)

from typing import List, Optional

from LeetCode.tree.TreeNode import TreeNode


class Solution:
    """ 501. 二叉搜索树中的众数
    """
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        prev:TreeNode = None
        cnt = 0
        mx_cnt = 0
        def dfs(root):
            nonlocal cnt, prev, mx_cnt
            if root is None:
                return
            dfs(root.left)
            if prev is None:
                cnt = 1
            elif prev.val == root.val:
                cnt += 1
            else: # prev.val != root.val
                cnt = 1
            prev = root

            if cnt == mx_cnt:
                ans.append(root.val)
            if cnt > mx_cnt:
                mx_cnt = cnt
                ans.clear()
                ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans

    """ 530. 二叉搜索树的最小绝对差
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev:TreeNode = None
        def dfs(root):
            nonlocal ans, prev
            if root is None:
                return
            dfs(root.left)
            if prev is not None:
                diff = root.val - prev.val
                ans = min(ans, diff)
            prev = root
            dfs(root.right)
        dfs(root)
        return ans
