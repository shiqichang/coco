# 03 对称二叉树

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 `[1,2,2,3,4,4,3]` 是对称的。

```shell
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```shell
    1
   / \
  2   2
   \   \
   3    3
```

### 进阶

你可以运用递归和迭代两种方法解决这个问题吗？

## 题解

```python
def is_symmetric(root):
    """ 递归 """
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

```python
def is_symmetric(root):
    """ 迭代 """
    if not root or not (root.left or root.right):
        return True
    # 用队列保存结点
    queue = [root.left, root.right]
    while queue:
        # 从队列中取出两个结点，再比较这两个结点
        left = queue.pop(0)
        right = queue.pop(0)
        # 如果两个结点都为空就继续循环，再者有一个为空就返回 false
        if not (left or right):
            continue
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        # 将左结点的左孩子，右结点的右孩子放入队列
        queue.append(left.left)
        queue.append(right.right)
        # 将左结点的右孩子，右结点的左孩子放入队列
        queue.append(left.right)
        queue.append(right.left)
    return True
```

🍥 **考察要点**：递归、迭代、队列
🍬 **解题思路**：递归；迭代。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
