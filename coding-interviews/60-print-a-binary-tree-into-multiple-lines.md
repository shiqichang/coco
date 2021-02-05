# 60 把二叉树打印成多行

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

## 题解

```python
import collections

def level_order(root):
    if not root:
        return []
    res, deque = [], collections.deque([root])
    while deque:
        tmp = []
        for _ in range(len(deque)):
            node = deque.popleft()
            tmp.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        res.append(tmp)
    return res
```

🍥 **考察要点**：二叉树、队列
🍬 **解题思路**：层序遍历。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
