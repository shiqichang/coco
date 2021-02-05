# 57 二叉树的下一个结点

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

## 题解

```python
def get_next(pNode):
    if not pNode:
        return None

    if pNode.right:
        p = pNode.right
        while p.left:
            p = p.left
        return p

    p = pNode
    while True:
        if p.next and p.next.left == p:
            return p.next
        if not p.next:
            return None
        p = p.next
```

🍥 **考察要点**：树
🍬 **解题思路**：暴力解法；最优解法。

- 有右子树，下一结点是右子树的最左结点；
- 无右子树，且结点是其父结点的左子树，则下一结点是其父结点；
- 无右子树，且结点是其父节点的右子树，则一直沿父结点追溯，直到找到某个结点是其父结点的左子树，那么这个结点的父结点就是要找的下一个结点。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
