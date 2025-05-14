# 144. 二叉树的前序遍历
# https://leetcode.cn/problems/binary-tree-preorder-traversal/description/

# 94. 二叉树的中序遍历
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

# 145. 二叉树的后序遍历
# https://leetcode.cn/problems/binary-tree-postorder-traversal/description/

from typing import Optional, List
from LeetCode.tree import TreeNode

class Solution:
    """ 通过迭代前序遍历二叉树
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur_node:TreeNode = root
        stack = []
        while cur_node or stack:
            while cur_node:
                ans.append(cur_node.val)
                stack.append(cur_node)
                cur_node = cur_node.left
            node = stack.pop()
            cur_node = node.right
        return ans

    """ 通过迭代中序遍历二叉树
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur_node:TreeNode = root
        stack = []
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            node = stack.pop()
            ans.append(node.val)
            cur_node = node.right
        return ans

    """ 通过迭代后续遍历二叉树
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur_node:TreeNode = root
        last:TreeNode = root
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack[-1] # 先使用，不pop
            # 当前节点右节点为空，或者已经访问过，则可以处理中节点（右中）
            if not cur_node.right or cur_node.right == last:
                ans.append(cur_node.val) # 处理当前节点
                stack.pop() # 删除节点
                last = cur_node # 更新上次处理的节点，上一层节点还会用到
                cur_node = None  # 将cur_node置空，下一轮从栈顶取新的元素
            else:
                cur_node = cur_node.right # 否则，处理右节点
        return ans

    # 递归
    def traversal_by_recur(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(cur_node):
            if not cur_node:
                return
            ans.append(cur_node.val) # 调整与dfs的相对顺序，决定是前序/中序/后序
            dfs(cur_node.left)
            dfs(cur_node.right)
        dfs(root)
        return ans
