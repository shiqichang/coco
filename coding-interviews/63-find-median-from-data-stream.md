# 63 数据流中的中位数

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

## 题解

```python
# 排序法
class Solution(object):
    def __init__(self):
        self.arr = []
        
    def Insert(self, num):
        self.arr.append(num)
        
    def GetMedian(self, sortedArr):
        sortedArr = sorted(self.arr)
        length = len(self.arr)
        mid = length / 2
        if length % 2 == 0:
            median = (sortedArr[mid-1] + sortedArr[mid]) / 2.0
        else:
            median = sortedArr[mid]
        return median
```

```python
# 二分查找插入
import bisect

class Solution(object):
    def __init__(self):
        self.d = []

    def insert(self, num):
        if not self.d:
            self.d.append(num)
        else:
            bisect.insort_left(self.d, num)  # 插入

    def get_median(self):
        n = len(self.d)
        if n & 1 == 1:  # n 是奇数
            return self.d[n // 2]
        else:
            return (self.d[n // 2] + self.d[n // 2 - 1]) / 2
```

```python
# 优先队列（堆）
import heapq

class Solution(object):
    def __init__(self):
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    def insert(self, num):
        if len(self.max_heap) == len(self.min_heap):  # 先加到大顶堆，再把大顶堆元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小顶堆元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]
```

🍥 **考察要点**：排序、二分查找、堆
🍬 **解题思路**：**排序法**，时间复杂度为 O(nlogn)；**二分查找插入**，时间复杂度为 O(n)；**优先队列（堆）**，将中位数左边的数保存在大顶堆，右边的数保存在小顶堆。*Python 中没有大顶堆，只能将值取负保存在小顶堆来模拟。*

🍉 **时间复杂度**：O(logn)
🍭 **空间复杂度**：O(n)
