# 19 顺时针打印矩阵

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

## 题解

```python
def print_matrix(matrix):
    ret = []
    while matrix:
        ret += (matrix.pop(0))
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix and matrix[0]:
            ret += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    return ret
```

🍥 **考察要点**：矩阵

🍬 **解题思路**：完成信息的索引与去除，按照顺时针，每打印一圈的同时删除一圈，再进入下一层循环。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
