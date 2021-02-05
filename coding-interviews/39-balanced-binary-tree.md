# 39 平衡二叉树

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一棵二叉树，判断该二叉树是否是平衡二叉树。在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树

## 题解

```python
def is_balanced(root):
    """ 自顶向下 """
    def height(root):
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1

    if not root:
        return True
    return abs(height(root.left) - height(root.right)) <= 1 and is_balanced(root.left) and is_balanced(root.right)
```

```python
def is_balanced(root):
    """ 自底向上 """
    def height(root):
        if not root:
            return 0
        left_height = height(root.left)
        right_height = height(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1

    return height(root) >= 0
```

🍥 **考察要点**：树、递归
🍬 **解题思路**：**平衡二叉树**的定义是左子树的高度与右子树的高度差的绝对值小于等于1. 而且其左/右子树也是平衡二叉树。

- **自顶向下**：*height(p) = max(height(p.left), height(p.right)) + 1*，p为非空结点，类似于二叉树的**前序遍历**。**时间复杂度**为 O(n^2).
- **自底向上**：类似于**后序遍历**。先递归判断左右子树是否平衡，再判断以当前结点为根的子树是否平衡。若是平衡树就返回其高度。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
