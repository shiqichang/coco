# 21 栈的压入、弹出序列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

## 题解

```python
def is_pop_order(pushV, popV):
    if not popV or len(pushV) != len(popV):
        return False
    stack, j = [], 0
    for i in range(len(pushV)):
        stack.append(pushV[i])
        while stack and stack[-1] == popV[j]:
            stack.pop()
            j += 1
    return len(stack) == 0
```

```python
def is_pop_order(pushV, popV):
    stack = []
    while popV:
        if stack and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
        elif pushV:
            stack.append(pushV.pop(0))
        else:
            return False
    return True
```

🍥 **考察要点**：栈
🍬 **解题思路**：新建一个栈，将数组 A 压入栈中，当栈顶元素等于数组 B 时，就将其出栈，当循环结束时，判断栈是否为空，若为空则返回 true.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
