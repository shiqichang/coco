# 05 用两个栈实现队列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

## 题解

```python
class Solution(object):
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
```

```java
import java.util.Stack;

public class Solution {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
        stack1.push(node);
    }
    
    public int pop() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
}
```

🍥 **考察要点**：队列、栈
🍬 **解题思路**：栈是 FILO, 队列是 FIFO.

- 插入时直接插入 stack1;
- 弹出时，当 stack2 不为空，弹出 stack2 栈顶元素，如果 stack2 为空，将 stack1 的全部逐个出栈入栈 stack2，再弹出 stack2 栈顶元素。

🍉 **时间复杂度**：O(1)
🍭 **空间复杂度**：O(n)
