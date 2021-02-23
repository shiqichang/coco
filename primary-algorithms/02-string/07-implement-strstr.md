# 07 实现 strStr()

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

### 示例1

> 输入: haystack = "hello", needle = "ll"
> 输出: 2

### 示例2

> 输入: haystack = "aaaaa", needle = "bba"
> 输出: -1

### 说明

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

## 题解

```python
def strstr(haystack, needle):
    """ 朴素匹配 """
    if needle == '':
        return 0

    a, b, c = 0, 0, 0  # a记录起点，b为haystack的滑动指针, c为needle的滑动指针
    while b < len(haystack):
        if haystack[b] == needle[c]:
            b += 1
            c += 1
        else:  # 重置
            a += 1
            b = a
            c = 0

        if c == len(needle):
            return a
    return -1
```

```python
def strstr(haystack, needle):
    """ KMP算法 """
    if needle == '':
        return 0
    n = len(needle)
    m = len(haystack)
    j = 0
    pnext = getnext(needle)
    for i in range(m):
        while j > 0 and needle[j] != haystack[i]:
            j = pnext[j]
        if needle[j] == haystack[i]:
            j += 1
            if j == n:
                return i-n+1
    return -1


def getnext(s):
    n = len(s)
    pnext = [0, 0]  # 多一个前导0是为了方便后续指针跳跃，避免死循环
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pnext[j]  # 跳跃指针
        if s[j] == s[i]:
            j += 1
        pnext.append(j)
    return pnext
```

```python
def strstr(haystack, needle):
    """ 内置函数 """
    if not needle:
        return 0
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1
```

🍥 **考察要点**：KMP 算法

🍬 **解题思路**：朴素匹配法，暴力匹配 BF，时间复杂度为 O(mn)；KMP 匹配法，需要使用一个**跳跃数组**，*每次遇到不同的字符后，就将指针跳跃到后缀字符串中部分匹配的位置。*永不回溯。

🍉 **时间复杂度**：O(m+n)

🍭 **空间复杂度**：O(n)
