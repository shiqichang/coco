# 24 二叉树中和为某一值的路径

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

## 题解

```python
def find_path(root, expectNumber):
    res, path = [], []

    def recur(root, tar):
        if not root:
            return
        path.append(root.val)
        tar -= root.val
        if tar == 0 and not root.left and not root.right:
            res.append(list(path))  # 复制一个 path
        recur(root.left, tar)
        recur(root.right, tar)
        path.pop()
    recur(root, expectNumber)
    return res
```

🍥 **考察要点**：树、递归

🍬 **解题思路**：**回溯法**，包括先序遍历和路径记录。

- 路径记录：记录从根结点到当前结点的路径。当路径为根结点到叶子结点形成的路径，并且各结点值的和等于 target.

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
