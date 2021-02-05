# 11 旋转图像

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个 *n* × *n* 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
**说明：** 你必须在**[原地](https://baike.baidu.com/item/原地算法)**旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要**使用另一个矩阵来旋转图像。

### 示例1

> 给定 matrix =
> [
> [1,2,3],
> [4,5,6],
> [7,8,9]
> ],
>
> 原地旋转输入矩阵，使其变为:
> [
> [7,4,1],
> [8,5,2],
> [9,6,3]
> ]

### 示例2

> 给定 matrix =
> [
> [ 5, 1, 9,11],
> [ 2, 4, 8,10],
> [13, 3, 6, 7],
> [15,14,12,16]
> ],
>
> 原地旋转输入矩阵，使其变为:
> [
> [15,13,2,5],
> [14, 3, 4, 1],
> [12, 6, 8, 9],
> [16, 7,10,11]
> ]

## 题解

```python
def rotate(matrix):
    """ 转置➕翻转 """
    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reverse each row
    for i in range(n):
        matrix[i].reverse()
```

```python
def rotate(matrix):
    """ 旋转4个矩形 """
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            row, col = i, j
            print(row, col)
            # store 4 elements in tmp
            for k in range(4):
                tmp[k] = matrix[row][col]
                row, col = col, n - 1 - row
            # rotate 4 elements
            for k in range(4):
                matrix[row][col] = tmp[(k - 1) % 4]
                row, col = col, n - 1 - row
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giz75a1oecj30xo0kiq90.jpg)

```python
def rotate(matrix):
    """ 在单次循环中旋转4个矩阵 """
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
```

🍥 **考察要点**：转置、翻转
🍬 **解题思路**：转置➕翻转；旋转四个矩形，可以在第一个矩阵中移动元素并且在长度为 `4` 个元素的临时列表中移动它们；在单次循环中旋转4个矩形

🍉 **时间复杂度**：O(n^2)
🍭 **空间复杂度**：O(1)
