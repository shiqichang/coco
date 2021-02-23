# 04 有效的字母异位词

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定两个字符串 *s* 和 *t* ，编写一个函数来判断 *t* 是否是 *s* 的字母异位词。

### 示例1

> 输入: s = "anagram", t = "nagaram"
> 输出: true

### 示例2

> 输入: s = "rat", t = "car"
> 输出: false

### 说明

你可以假设字符串只包含小写字母。

### 进阶

如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

## 题解

```python
import collections

def is_anagram(s, t):
    """ 哈希表 """
    return collections.Counter(s) == collections.Counter(t)
```

```python
def is_anagram(s, t):
    """ 排序法 """
    return sorted(s) == sorted(t)
```

🍥 **考察要点**：排序、哈希表

🍬 **解题思路**：排序法，时间复杂度为 O(nlogn)；哈希表。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
