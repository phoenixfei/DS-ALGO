在 Python 中操作二维数组时，使用一些 Pythonic（符合 Python 风格） 的技巧可以让代码更简洁、优雅、高效。以下是一些常用且实用的技巧，适用于嵌套列表（非 NumPy 环境）：

⸻

一、转置二维数组（行变列）

grid = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = list(zip(*grid))
# [(1, 4), (2, 5), (3, 6)]


⸻

二、二维数组的列表推导式

1. 平铺二维数组（flatten）

flat = [x for row in grid for x in row]
# [1, 2, 3, 4, 5, 6]

2. 创建二维数组（初始化）

grid = [[0] * 3 for _ in range(2)]
# [[0, 0, 0], [0, 0, 0]]

注意：不要用 [[0]*3]*2，因为那样会创建两个引用相同的子列表！

⸻

三、按列/行取值

取第 i 列：

i = 1
column = [row[i] for row in grid]

取第 i 行：

row = grid[i]


⸻

四、条件筛选 / 条件替换

将所有奇数变为 0：

new_grid = [[x if x % 2 == 0 else 0 for x in row] for row in grid]


⸻

五、查找最大值及其位置

max_val = max(max(row) for row in grid)
positions = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == max_val]


⸻

六、旋转二维数组

1. 顺时针旋转 90 度：

rotated = [list(row)[::-1] for row in zip(*grid)]

2. 逆时针旋转 90 度：

rotated = list(zip(*grid[::-1]))


⸻

七、二维数组中任意值是否满足某条件

any_odd = any(x % 2 != 0 for row in grid for x in row)
all_positive = all(x > 0 for row in grid for x in row)


⸻

八、使用 enumerate 获取坐标和值

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        print(f"grid[{i}][{j}] = {val}")


⸻

九、zip 配合多个二维数组

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

summed = [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
# [[6, 8], [10, 12]]


⸻

如果你经常处理大量二维数组数据，考虑用 NumPy 会更高效。你想我也列一份 NumPy 的版本吗？