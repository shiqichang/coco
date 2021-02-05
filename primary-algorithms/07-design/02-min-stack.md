# 02 最小栈

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

- push(x) —— 将元素 x 推入栈中。
- pop() —— 删除栈顶的元素。
- top() —— 获取栈顶元素。
- getMin() —— 检索栈中的最小元素。

### 示例

> 输入：
> ["MinStack","push","push","push","getMin","pop","top","getMin"]
> [[],[-2],[0],[-3],[],[],[],[]]
>
> 输出：
> [null,null,null,null,-3,null,0,-2]
>
> 解释：
> MinStack minStack = new MinStack();
> minStack.push(-2);
> minStack.push(0);
> minStack.push(-3);
> minStack.getMin();   --> 返回 -3.
> minStack.pop();
> minStack.top();      --> 返回 0.
> minStack.getMin();   --> 返回 -2.

### 进阶

- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用。

## 题解

```python
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
```

🍥 **考察要点**：辅助栈
🍬 **解题思路**：**辅助栈。**当元素要入栈时，取当前辅助栈的栈顶元素，与当前元素比较得出最小值，将这个最小值插入辅助栈；当元素要出栈时，把辅助栈的栈顶元素一并弹出。

🍉 **时间复杂度**：O(1)
🍭 **空间复杂度**：O(n)
