# 06 两个数组的交集 II

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定两个数组，编写一个函数来计算它们的交集。

### 示例1

> 输入：nums1 = [1,2,2,1], nums2 = [2,2]
>
> 输出：[2, 2]

### 示例2

> 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
>
> 输出：[4, 9]

### 说明

- 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
- 我们可以不考虑输出结果的顺序。

### 进阶

- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
- 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

## 题解

```python
import collections

def intersect(nums1, nums2):
    num1 = collections.Counter(nums1)
    num2 = collections.Counter(nums2)
    num = num1 & num2
    return num.elements()
```

```python
import collections

def intersect(nums1, nums2):
    """ 哈希表 """
    if len(nums1) > len(nums2):
        return intersect(nums2, nums1)  # 先遍历较短的数组并在哈希表中记录，降低空间复杂度

    # 遍历第一个数组，创建哈希表
    m = collections.Counter()
    for num in nums1:
        m[num] += 1

    # 遍历第二个数组
    intersection = []
    for num in nums2:
        if m.get(num, 0) > 0:
            intersection.append(num)
            m[num] -= 1  # 减少哈希表中该数字出现的次数
            if m[num] == 0:
                m.pop(num)

    return intersection
```

```python
def intersect(nums1, nums2):
    """ 排序➕双指针法 """
    nums1.sort()
    nums2.sort()
    
    len1, len2 = len(nums1), len(nums2)
    intersection = []
    i = j = 0
    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            intersection.append(nums1[i])
            i += 1
            j += 1
            
    return intersection
```

🍥 **考察要点**：排序、哈希表
🍬 **解题思路**：给定数组未排序选择**哈希表法**，排序选择**双指针法**。

- **哈希表**：时间复杂度为 *O(m+n)*, 空间复杂度为 *O(min(m, n))*；
- **排序➕双指针法**：初始时，两个指针分别指向两个数组的头部，比较指针指向的数字，如果不想等，将**较小数字**的指针右移一位，否则将数字添加到结果中，并同时右移一位，当至少有一个指针超出数组范围，遍历结束。

🍉 **时间复杂度**：O(mlogm + nlogn)
🍭 **空间复杂度**：O(min(m, n))
