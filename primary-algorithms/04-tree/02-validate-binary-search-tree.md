# 02 验证二叉搜索树

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

### 示例1

> 输入:
>
> ```shell
>   2
>  / \
> 1  3
> ```
>
> 输出: true

### 示例2

> 输入:
>
> ```shell
>     5
>    / \
>   1   4
>      / \
>     3   6
> ```
>
> 输出: false
> 解释: 输入为: [5,1,4,null,null,3,6]。
> 根节点的值为 5 ，但是其右子节点值为 4 。

## 题解

```python
def is_valid_bst(root):
    """ 递归 """
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True
    
    return helper(root)
```

```python
def is_valid_bst(root):
    """ 中序遍历 """
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # 如果中序遍历得到的结点的值小于等于前一个 inorder, 说明不是二叉搜索树
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True
```

🍥 **考察要点**：递归、中序遍历
🍬 **解题思路**：递归；中序遍历，二叉搜索树的中序遍历结果是升序序列。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
