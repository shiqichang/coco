# 09 最长公共前缀

> 🌈 **初级算法系列之字符串**
>
> 你的无畏源于无知。

## 题目描述

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 `""`。

### 示例1

> 输入: ["flower","flow","flight"]
> 输出: "fl"

### 示例2

> 输入: ["dog","racecar","car"]
> 输出: ""
> 解释: 输入不存在公共前缀。

### 说明

所有输入只包含小写字母 `a-z` 。

## 题解

```python
def longest_common_prefix(strs):
    """ 横向扫描 """
    if not strs:
        return ""
    prefix, count = strs[0], len(strs)
    for i in range(1, count):
        prefix = lcp(prefix, strs[i])
        if not prefix:
            break

    return prefix


def lcp(str1, str2):
    length, index = min(len(str1), len(str2)), 0
    while index < length and str1[index] == str2[index]:
        index += 1
    return str1[:index]
```

```python
def longest_common_prefix(strs):
    """ 纵向扫描 """
    if not strs:
        return ""
    length, count = len(strs[0]), len(strs)
    for i in range(length):
        c = strs[0][i]
        if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
            return strs[0][:i]

    return strs[0]
```

```python
def longest_common_prefix(strs):
    """ 分治 """
    def lcp(start, end):
        if start == end:
            return strs[start]

        mid = (start + end) // 2
        lcp_left, lcp_right = lcp(start, mid), lcp(mid + 1, end)
        min_length = min(len(lcp_left), len(lcp_right))
        for i in range(min_length):
            if lcp_left[i] != lcp_right[i]:
                return lcp_left[:i]

        return lcp_left[:min_length]

    return '' if not strs else lcp(0, len(strs) - 1)
```

```python
def longest_common_prefix(strs):
    """ 二分查找 """
    def is_common_prefix(length):
        str0, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == str0 for i in range(1, count))

    if not strs:
        return ''

    min_length = min(len(s) for s in strs)
    low, high = 0, min_length
    while low < high:
        mid = (high - low + 1) // 2 + low
        if is_common_prefix(mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]
```

🍥 **考察要点**：横向扫描、纵向扫描、分治、二分查找

🍬 **解题思路**：横向扫描；纵向扫描；分治；二分查找，时间复杂度为 O(mnlogm).

🍉 **时间复杂度**：O(mn)

🍭 **空间复杂度**：O(1)
