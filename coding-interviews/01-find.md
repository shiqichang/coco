# 01 二维数组中的查找

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

## 题解

```python
def find(target, array):
    if array is None:
        return False

    i, j = 0, len(array[0]) - 1
    while i < len(array) and j >= 0:
        tmp = array[i][j]
        if target > tmp:
            i += 1
        elif target < tmp:
            j -= 1
        else:
            return True

    return False
```

🍥 **考察要点**：数组、二分查找

🍬 **解题思路**：从二维数组的右上方开始查找。

🍉 **时间复杂度**：O(n+m)

🍭 **空间复杂度**：O(1)
