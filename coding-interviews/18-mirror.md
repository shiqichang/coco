# 18 二叉树的镜像

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

操作给定的二叉树，将其变换为源二叉树的镜像。

## 题解

```python
def mirror(pRoot):
    """ 递归版本 """
    if not pRoot:
        return
    mirror(pRoot.left)
    mirror(pRoot.right)
    pRoot.left, pRoot.right = pRoot.right, pRoot.left
```

```python
def mirror(pRoot):
    """ 非递归版本 """
    if not pRoot:
        return
    pq = list()
    pq.append(pRoot)
    while pq:
        node = pq.pop(0)
        if not node:
            return
        if node.left:
            pq.append(node.left)
        if node.right:
            pq.append(node.right)
        node.left, node.right = node.right, node.left
```

🍥 **考察要点**：数、递归
🍬 **解题思路**：树的后序遍历和层次遍历。

- 递归版本：树的后序遍历 (LRD, Postorder Traversal) 是左右根。
- 非递归版本：树的层次遍历，利用栈实现。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
