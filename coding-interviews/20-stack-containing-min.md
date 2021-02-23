# 20 包含min函数的栈

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

## 题解

```python
class Solution(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, node):
        self.stack.append(node)
        if not self.mins or node <= self.mins[-1]:
            self.mins.append(node)

    def pop(self):
        if self.stack and (self.stack.pop() == self.mins[-1]):
            self.mins.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.stack:
            return self.mins[-1]
```

```python
class Solution(object):

    def __init__(self):
        self.stack = []

    def push(self, node):
        cur_min = self.min()
        if not cur_min or node <= cur_min:
            self.stack.append((node, node))
        else:
            self.stack.append((node, cur_min))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def min(self):
        if self.stack:
            return self.stack[-1][1]
```

🍥 **考察要点**：栈

🍬 **解题思路**：使用辅助栈 B，专门用于获取最小值，它是**非严格降序**的。还有一种思路，栈存储二元组，包含入栈元素和当前最小元素。

🍉 **时间复杂度**：O(1)

🍭 **空间复杂度**：O(n)
