from typing import List


class Solution:
    # [51. N皇后](https://leetcode.cn/problems/n-queens/description/)
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        path = [["."] * n for _ in range(n)]
        print(path)

        def check(r, c) -> bool:
            # 从第0行开始往下走，故不需要行check
            # 列check
            for i in range(r):
                if path[i][c] == 'Q':
                    return False
            # 右上角check
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if path[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # 左上角check
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if path[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            return True

        def dfs(i):
            if i == n:
                ans.append(["".join(item) for item in path])
                return
            for j in range(n):
                if check(i, j):
                    path[i][j] = 'Q'
                    dfs(i + 1)
                    path[i][j] = '.'

        dfs(0)
        return ans


    # [37. 解数独](https://leetcode.cn/problems/sudoku-solver/description/)
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        rn = [[False] * n for _ in range(n)]
        cn = [[False] * n for _ in range(n)]
        xn = [[[False] * n for _ in range(n//3)] for _ in range(3)]
        space = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    space.append((i, j))
                else:
                    d = int(board[i][j]) - 1
                    rn[i][d] = True
                    cn[j][d] = True
                    xn[i//3][j//3][d] = True

        def dfs(cnt) -> bool:
            if cnt == len(space):
                return True
            i, j = space[cnt]
            for d in range(n):
                if rn[i][d] == cn[j][d] == xn[i//3][j//3][d] == False:
                    rn[i][d] = cn[j][d] = xn[i // 3][j // 3][d] = True
                    board[i][j] = str(d+1)
                    if dfs(cnt+1):
                        return True
                    rn[i][d] = cn[j][d] = xn[i // 3][j // 3][d] = False
            return False
        dfs(0)