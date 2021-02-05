# 42 和为S的两个数字

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

### 输入描述

> 对应每个测试案例，输出两个数，小的先输出。

## 题解

```python
def find_numbers_with_sum(nums, target):
    """ 双指针法 """
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            return nums[i], nums[j]
    return []
```

🍥 **考察要点**：数组、哈希、双指针
🍬 **解题思路**：利用 HashMap 可以通过遍历数组找到数字组合，时间/空间复杂度均为 O(n); 由于是排序数组，所以可以通过**双指针法**降低空间复杂度。

- 初始化：i, j 分别指向数组的左右两端（俗称对撞双指针）；
- 循环搜索：`s = nums[i] + nums[j]`, 若 `s > target` 则 `j--`; 若 `s < target` 则 `i++`.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
