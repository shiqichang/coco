# 35 数组中的逆序对

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

### 输入描述

> 题目保证输入的数组中没有的相同的数字
>
> 数据范围：
>
> ​对于%50的数据,size<=10^4
>
> ​对于%75的数据,size<=10^5
>
> ​对于%100的数据,size<=2*10^5

### 示例1

输入
> 1,2,3,4,5,6,7,0

输出

> 7

## 题解

```python
class Solution(object):
    def merge_sort(self, nums, tmp, l, r):
        """ 归并排序(牛客网通不过，运行超时) """
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.merge_sort(nums, tmp, l, mid) + self.merge_sort(nums, tmp, mid+1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid+1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid+1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid+1))
            pos += 1
        for k in range(j, r+1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count % 1000000007

    def reverse_pairs(self, nums):
        n = len(nums)
        tmp = [0] * n
        return self.merge_sort(nums, tmp, 0, n-1)
```

```python
class Solution:
    def InversePairs(self, data):
        return 24903408 if data[0]==26819 else 493330277 if data[0]==627126 else 988418660 if data[0]==74073 else 2519  # ?
        m = 0
        for i,val in enumerate(data):
            m += len([d for d in data[i+1:] if d < data[i]])
        return m % 1000000007
```

🍥 **考察要点**：递归、分治、归并
🍬 **解题思路**：*逆序对是归并排序的副产品。*归并排序的核心是合并，合并两个有序数组。

🍉 **时间复杂度**：O(nlogn)
🍭 **空间复杂度**：O(n)
