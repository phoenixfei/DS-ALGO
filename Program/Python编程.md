# Pythonic编程技巧
在 Python 中操作二维数组时，使用一些 Pythonic（符合 Python 风格） 的技巧可以让代码更简洁、优雅、高效。以下是一些常用且实用的技巧，适用于嵌套列表（非 NumPy 环境）：

---

## 列表操作

### 一、转置二维数组（行变列）

`*grid`表示解包。 

>在 Python 中，解包（unpacking） 是一种将“可迭代对象”的元素拆解出来，并分别赋值给变量的语法。它非常常见且强大，可以用于元组、列表、字符串、字典等。
> 
> 基本解包：`x, y, z = (10, 20, 30)`
> 
> 使用*号进行扩展解包: `a, *b = [1, 2, 3, 4]` ，解包后，a为1; b为列表[2, 3, 4]。

解包后，用zip将行对应的列表“打包”在一起，再转成list形式，即可得到转置后的矩阵。
> Python 中的 zip() 是一个非常实用的内置函数，用于将多个可迭代对象“打包”在一起，生成一个由元组组成的迭代器，每个元组包含来自所有输入可迭代对象中对应位置的元素。

```python
grid = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = list(zip(*grid))
# [(1, 4), (2, 5), (3, 6)]
```

---

### 二、二维数组的列表推导式

1. 平铺二维数组（flatten）
   ```python
    flat = [x for row in grid for x in row]
    # [1, 2, 3, 4, 5, 6]
    ```
2. 创建二维数组（初始化）
    ```python
    grid = [[0] * 3 for _ in range(2)]
    # [ [0, 0, 0], [0, 0, 0]]
    ```
   注意：不要用 `[[0]*3]*2`，因为那样会创建两个引用相同的子列表！

---

### 三、条件筛选 / 条件替换

将所有奇数变为 0：
`new_grid = [[x if x % 2 == 0 else 0 for x in row] for row in grid]`

---

### 四、查找最大值及其位置
```python
max_val = max(max(row) for row in grid)
positions = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == max_val]
```

---

### 五、旋转二维数组

1. 顺时针旋转 90 度：
`rotated = [list(row)[::-1] for row in zip(*grid)]`

2. 逆时针旋转 90 度：
`rotated = list(zip(*grid[::-1]))`

---

### 七、二维数组中任意值是否满足某条件
`any_odd = any(x % 2 != 0 for row in grid for x in row)`
`all_positive = all(x > 0 for row in grid for x in row)`

---

### 八、使用 enumerate 获取坐标和值
```python
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        print(f"grid[{i}][{j}] = {val}")
```

---

### 九、zip 配合多个二维数组
```python
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

summed = [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
# [[6, 8], [10, 12]]
```
