# 03 从尾到头打印链表

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

## 题解

```python
class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def print_list_from_tail_to_head(list_node):
    from collections import deque
    stack = deque()
    while list_node:
        stack.appendleft(list_node.val)
        list_node = list_node.next
    return stack
```

🍥 **考察要点**：单链表、递归、反转链表

🍬 **解题思路**：利用**栈**存储。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)

其他方法有 **递归**  `func(node.next); ret.append(node.val)`、遍历再 **逆序** 输出 `ret[::-1]`.
