# 58 对称的二叉树

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

## 题解

```python
def is_symmetric(root):
    if not root:
        return True

    def dfs(left, right):
        # 递归的终止条件是两个结点都为空
        # 或者两个结点中有一个为空
        # 或者两个结点的值不相等
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)
    # 用递归函数，比较左结点，右结点
    return dfs(root.left, root.right)
```

🍥 **考察要点**：二叉树、递归

🍬 **解题思路**：判断该二叉树和它的镜像是否相同。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
