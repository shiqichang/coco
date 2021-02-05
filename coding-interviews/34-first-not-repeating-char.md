# 34 第一个只出现一次的字符

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）

## 题解

```python
def first_not_repeating_char(s):
    if not s:
        return -1
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1
```

```python
def first_not_repeating_char(s):
    """ 哈希表 """
    dic = {}
    for c in s:
        dic[c] = not c in dic
    # for c in s:
    #     if dic[c]:
    #         return s.index(c)
    for k, v in dic.items():
        if v: return s.index(k)
    return -1
```

🍥 **考察要点**：哈希，bitset
🍬 **解题思路**：`c in dic` 判断字典中是否含有键 `c`.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
