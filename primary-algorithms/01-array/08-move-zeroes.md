# 08 移动零

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

### 示例

> 输入: [0,1,0,3,12]
> 输出: [1,3,12,0,0]

### 说明

1. 必须在原数组上操作，不能拷贝额外的数组。
2. 尽量减少操作次数。

## 题解

```python
def move_zeroes(nums):
    """ 两次遍历 """
    if not nums:
        return
    # 第一次遍历，j 指针记录非0的个数，只要是非0的就赋值给 nums[j]
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j] = nums[i]
            j += 1
    # 第二次遍历，把末尾的元素都赋给0
    for i in range(j, len(nums)):
        nums[i] = 0
```

```python
def move_zeroes(nums):
    """ 一次遍历 """
    if not nums:
        return
    # 两个指针 i 和 j
    j = 0
    for i in range(len(nums)):
        # 当前元素!=0, 就把其交换到左边，等于0的交换到右边
        if nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
```

🍥 **考察要点**：双指针法
🍬 **解题思路**：双指针法，一次遍历；二次遍历，参考快速排序的思想，用 `0` 作为中间点，不等于0的放在中间点的左边，等于0的放在其右边。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
