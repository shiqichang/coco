# 03 字符串中第一个唯一字符

> 🌈 **初级算法系列之字符串**
>
> 你的无畏源于无知。

## 题目描述

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

### 示例

> s = "leetcode"
> 返回 0
>
> s = "loveleetcode"
> 返回 2

## 题解

```python
def first_uniq_char(s):
    cnt = collections.Counter(s)
    for idx, ch in enumerate(s):
        if cnt[ch] == 1:
            return idx
    return -1
```

🍥 **考察要点**：哈希表

🍬 **解题思路**：哈希表，线性时间复杂度解法。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
