# 37 数字在排序数组中出现的次数

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

统计一个数字在升序数组中出现的次数。

## 题解

```python
def search(nums, target):
    # return nums.count(target)
    # 搜索右边界 right
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] <= target:
            i = m + 1
        else:
            j = m - 1
    right = i
    # 若数组中无 target, 则提前返回
    if j >= 0 and nums[j] != target:
        return 0
    # 搜索左边界 left
    i = 0
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        else:
            j = m - 1
    left = j
    return right - left - 1
```

```python
def search(nums, target):
    def helper(tar):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= tar:
                i = m + 1
            else:
                j = m - 1
        return i
    return helper(target) - helper(target - 1)
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1girgdoq0hcj30pg0g20uw.jpg)

🍥 **考察要点**：数组、二分查找

🍬 **解题思路**：使用二分法分别找到**左边界** *left* 和**右边界** *right*，得 *target* 的数量为 *right - left - 1*.

- 优化：分别二分查找 *target* 和 *target-1* 的右边界，两结果相减并返回。

🍉 **时间复杂度**：O(logn)

🍭 **空间复杂度**：O(1)
