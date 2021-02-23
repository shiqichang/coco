# 09 两数之和

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

### 示例

> 给定 nums = [2, 7, 11, 15], target = 9
>
> 因为 nums[0] + nums[1] = 2 + 7 = 9
> 所以返回 [0, 1]

## 题解

```python
def two_sum(nums, target):
    """ 两遍哈希 """
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j and i != j:
            return [i, j]
```

```python
def two_sum(nums, target):
    """ 一遍哈希 """
    hashmap = {}
    for i, num in enumerate(nums):
        if (target - num) in hashmap:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i  # 这句不能放在 if 语句前，解决 list 中有重复值或 target-num=num 的情况
```

🍥 **考察要点**：哈希法

🍬 **解题思路**：一遍哈希或两遍哈希，判断 `num2 in nums`.

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
