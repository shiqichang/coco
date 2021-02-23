# 22 从上往下打印二叉树

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

## 题解

```python
def print_from_top_to_bottom(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
```

🍥 **考察要点**：二叉树、队列、树的层序遍历

🍬 **解题思路**：树的层序遍历，创建一个队列存储结点值。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
