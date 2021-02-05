# 54 字符流中第一个不重复的字符

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

### 输入描述

> 如果当前字符流没有存在出现一次的字符，返回#字符。

## 题解

```python
class Solution(object):
    def __init__(self):
        self.s = ''
        # self.list_count = [0]*256

    def first_appearing_once(self):
        for c in self.s:
            if self.s.count(c) == 1:
            # if self.list_count[ord(c)] == 1:
                return c
        return '#'

    def insert(self, char):
        self.s += char
        # self.list_count[ord(char)] += 1
```

🍥 **考察要点**：哈希、队列
🍬 **解题思路**：内置方法 `s.count(c)`; 哈希➕队列：新建数组，存储每个字符出现的次数。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
