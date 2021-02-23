# 50 数组中重复的数字

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

## 题解

```python
def duplicate(numbers, duplication):
    if numbers is None or len(numbers) < 0:
        return False
    for i in range(len(numbers)):
        while i != numbers[i]:
            if numbers[numbers[i]] == numbers[i]:
                duplication[0] = numbers[i]
                return True
            tmp = numbers[i]
            numbers[i] = numbers[tmp]
            numbers[tmp] = tmp
    return False
```

🍥 **考察要点**：数组、哈希

🍬 **解题思路**：数组➕哈希；**in-place算法**。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
