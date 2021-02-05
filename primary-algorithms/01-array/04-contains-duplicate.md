# 04 存在重复元素

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 `true` 。如果数组中每个元素都不相同，则返回 `false` 。

### 示例1

> 输入: [1,2,3,1]
> 输出: true

### 示例2

> 输入: [1,2,3,4]
> 输出: false

### 示例3

> 输入: [1,1,1,3,3,4,3,2,4,2]
> 输出: true

## 题解

```python
def contains_duplicate(nums):
    return not len(nums) == len(set(nums))
```

```python
def contains_duplicate(nums):
    dic = {}
    for num in nums:
        if dic.get(num):
            return True
        dic[num] = 1
    return False
```

🍥 **考察要点**：哈希表、排序
🍬 **解题思路**：将数组转换成集合，比较数组和集合的长度；哈希表。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
