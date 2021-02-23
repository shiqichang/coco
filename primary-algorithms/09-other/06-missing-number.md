# 06 缺失数字

> 🌈 **初级算法系列之其它**
>
> 你的无畏源于无知。

## 题目描述

给定一个包含 `0, 1, 2, ..., n` 中 *n* 个数的序列，找出 0 .. *n* 中没有出现在序列中的那个数。

### 示例1

> 输入: [3,0,1]
> 输出: 2

### 示例2

> 输入: [9,6,4,2,3,5,7,0,1]
> 输出: 8

### 说明

你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

## 题解

```python
def missing_number(nums):
    """ 排序 """
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num
```

```python
def missing_number(nums):
    """ 哈希表 """
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number
```

```python
def missing_number(nums):
    """ 位运算 """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing
```

```python
def missing_number(nums):
    """ 数学 """
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

🍥 **考察要点**：排序、哈希表、位运算、数学

🍬 **解题思路**：排序，时间复杂度为 O(nlogn)；哈希表；位运算，将结果的初始值设为 n*n*，再对数组中的每一个数以及它的下标进行一个异或运算；数学，高斯公式。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
