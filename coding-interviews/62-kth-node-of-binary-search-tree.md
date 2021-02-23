# 62 二叉搜索树的第k个结点

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给定一棵二叉搜索树，请找出其中的第k小的结点。例如（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

## 题解

```python
class Solution(object):

    def __init__(self):
        self.index = 0

    def KthNode(self, root, k):
        if not root:
            return
        left = self.KthNode(root.left, k)
        if left:
            return left
        self.index += 1
        if self.index == k:
            return root
        right = self.KthNode(root.right, k)
        if right:
            return right
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giusbf8e0gj30li0fk0v0.jpg)

🍥 **考察要点**：二叉搜索树、中序遍历

🍬 **解题思路**：二叉搜索树的中序遍历是**递增序列**。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
