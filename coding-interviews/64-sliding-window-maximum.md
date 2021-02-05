# 64 滑动窗口的最大值

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。窗口大于数组长度的时候，返回空

## 题解

```python
def max_in_windows(num, size):
    """ 暴力法 """
    if not num or size <= 0:
        return []
    if len(num) < size:
        return []
    res = []
    for i in range(len(num)-size+1):
        print(i)
        tmp = num[i:i+size]
        if len(tmp) == size:
            res.append(max(tmp))
        else:
            break
    return res
```

```python
import collections

def max_in_windows(num, k):
    """ 双向队列 """
    n = len(num)
    if n * k == 0:
        return []
    if n < k:
        return []
    if k == 1:
        return num

    def clean_deque(i):
        # remove indexes of elements not from sliding window
        if deq and deq[0] == i - k:
            deq.popleft()

        # remove from deq indexes of all elements
        # which are smaller than current element num[i]
        while deq and num[i] > num[deq[-1]]:
            deq.pop()

    # init deque and output
    deq = collections.deque()
    max_idx = 0
    for i in range(k):
        clean_deque(i)
        deq.append(i)
        # compute max in num[i]
        if num[i] > num[max_idx]:
            max_idx = i
    output = [num[max_idx]]

    # build output
    for i in range(k, n):
        clean_deque(i)
        deq.append(i)
        output.append(num[deq[0]])
    return output
```

```python
def max_in_windows(num, k):
    """ 动态规划 """
    n = len(num)
    if n * k == 0:
        return []
    if n < k:
        return []
    if k == 1:
        return num

    left = [0] * n
    left[0] = num[0]
    right = [0] * n
    right[n-1] = num[n-1]
    for i in range(1, n):
        # from left to right
        if i % k == 0:
            # block start
            left[i] = num[i]
        else:
            left[i] = max(left[i-1], num[i])
        # from right to left
        j = n - i - 1
        if (j + 1) % k == 0:
            # block end
            right[j] = num[j]
        else:
            right[j] = max(right[j+1], num[j])

    output = []
    for i in range(n-k+1):
        # i+k-1 = j
        # max(right[i], left[j])
        output.append(max(left[i+k-1], right[i]))
        
    return output
```

🍥 **考察要点**：数组、队列
🍬 **解题思路**：

- **暴力法**，时间复杂度为 O(nk), 空间复杂度为 O(n-k+1)；
- **双向队列**：
  - 处理前 `k` 个元素，初始化双向队列；
  - 循环数组，清理双向队列（只保留当前窗口中有的元素索引，移除比当前元素小的元素）。
  - 将当前元素添加到双向队列，将 `deque[0]` 添加到输出中；
- **动态规划**：将输入数组分割成有 `k` 个元素的块。
  - 从左到右遍历数组，建立数组 `left`;
  - 从右到左遍历数组，建立数组 `right`;
  - 建立输出数组 `max(right[i], left[i+k-1])`, 其中 `i` 取值范围为 `(0, n-k+1)`.
  - `left[j]` 是从块的开始到下标 `j` 最大的元素，`right[j]` 是从块的结尾到下标 `j` 最大的元素。
  - 考虑从下标 `i` 到 `j` 的滑动窗口，`right[i]` 是左侧块内的最大元素，`left[j]` 是右侧块内的最大元素。故滑动窗口的最大元素是 `max(right[i], left[j])`.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
