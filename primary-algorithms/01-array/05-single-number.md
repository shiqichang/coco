# 05 只出现一次的数字

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

### 示例1

> 输入：[2, 2, 1]
>
> 输出：1

### 示例2

> 输入：[4, 1, 2, 1, 2]
>
> 输出：4

## 题解

```python
def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
```

```python
import functools

def single_number(nums):
    return functools.reduce(lambda x, y: x ^ y, nums)
```

🍥 **考察要点**：位运算、异或运算
🍬 **解题思路**：异或运算，相同为0，不同为1。使用 `reduce()` 内置函数。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
