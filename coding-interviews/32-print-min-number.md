# 32 把数组排成最小的数

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

## 题解

```python
import itertools

def print_min_number(numbers):
    """ 内置函数 itertools.permutations() """
    if not numbers:
        return ""
    numbers = list(map(str, numbers))
    res = list(map("".join, itertools.permutations(numbers)))
    return min(res)
```

```python
def print_min_number(nums):
    """ 快速排序(牛客网通不过，运行超时) """
    def fast_sort(l, r):
        if l >= r:
            return
        i, j = l, r
        while i < j:
            while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                i += 1
        strs[i], strs[l] = strs[l], strs[i]
        fast_sort(l, i-1)
        fast_sort(i+1, r)

    strs = [str(num) for num in nums]
    fast_sort(0, len(strs)-1)
    return ''.join(strs)
```

```python
import functools

def print_min_number(nums):
    """ 内置函数 functools.cmp_to_key() """
    def sort_rule(x, y):
        a, b = x + y, y + x
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    strs = [str(num) for num in nums]
    strs.sort(key=functools.cmp_to_key(sort_rule))
    return ''.join(strs)
```

🍥 **考察要点**：数组、全排列、排序、贪心
🍬 **解题思路**：**排序判断规则**是，若拼接字符串 `x+y > y+x`, 则 `m > n`.

🍉 **时间复杂度**：O(nlogn)
🍭 **空间复杂度**：O(n)
