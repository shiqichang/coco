# 01 合并两个有序数组

> 🌈 **初级算法系列之排序和搜索**
>
> 你的无畏源于无知。

## 题目描述

给你两个有序整数数组 *nums1* 和 *nums2*，请你将 *nums2* 合并到 *nums1* 中*，*使 *nums1* 成为一个有序数组。

### 说明

- 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
- 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

### 示例

> 输入:
> nums1 = [1,2,3,0,0,0], m = 3
> nums2 = [2,5,6],       n = 3
>
> 输出: [1,2,2,3,5,6]

## 题解

```python
def merge(nums1, m, nums2, n):
    """ 合并后排序 """
    nums1[:] = sorted((nums1[:m] + nums2))
```

```python
def merge(nums1, m, nums2, n):
    """ 双指针➕从前往后 """
    # Make a copy of nums1
    nums1_copy = nums1[:]
    nums1[:] = []

    # Two get pointers for nums1_copy and nums2
    p1 = 0
    p2 = 0
    
    # Compare elements from num1_copy and num2 
    # and add the smallest one into nums1
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1
            
    # if there are still elements to add
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]
```

```python
def merge(nums1, m, nums2, n):
    """ 双指针➕从后往前 """
    # two get pointers from nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    # set pointer from nums1
    p = m + n - 1

    # while there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    # add missing elements from num2
    nums1[:p2 + 1] = nums2[:p2 + 1]
```

🍥 **考察要点**：双指针

🍬 **解题思路**：合并后排序，时间复杂度为 O((n+m)log(n+m))；双指针➕从前往后，空间复杂度为 (m)；双指针➕从后往前。

🍉 **时间复杂度**：O(n+m)

🍭 **空间复杂度**：O(1)
