# 13 调整数组顺序使奇数位于偶数前面

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

## 题解

```python
def reorder_array(array):
    ret = list()
    for i in range(len(array)):
        if array[i] & 1:
            ret.append(array[i])
    for i in range(len(array)):
        if not array[i] & 1:
            ret.append(array[i])
    return ret
```

🍥 **考察要点**：数组
🍬 **解题思路**：创建一个新数组，对原数组进行两次遍历，第一次遍历遇到奇数插入新数组，第二次遍历遇到偶数插入新数组。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)

若要求不开辟额外数组，那么可以使用 **in-place 算法**, 此时**空间复杂度**为 `O(1)`, **时间复杂度**为 `O(n^2)`.

```python
class Solution:
    def reOrderArray(self , array ):
        # write code here
        i = 0
        for j in range(len(array)):
            if array[j] & 1:
                tmp = array[j]
                for k in range(j-1, i-1, -1):
                    array[k+1] = array[k]
                array[i] = tmp
                i += 1
        return array
```
