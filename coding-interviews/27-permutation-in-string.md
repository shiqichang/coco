# 27 字符串的排列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

### 输入描述

> 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

## 题解

```python
import itertools

def permutation(ss):
    if not ss:
        return []
    arr = sorted(set(list(map(''.join, itertools.permutations(ss)))))
    return arr
```

```python
def permutation(ss):
    if not ss:
        return []
    res = []

    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], tmp + nums[i])
    backtrack(ss, '')
    return sorted(list(set(res)))
```

🍥 **考察要点**：字符串、递归、回溯

🍬 **解题思路**：问题转换为先固定第一个字符，求剩余字符的排列。

🍉 **时间复杂度**：O(n!)

🍭 **空间复杂度**：O(1)
