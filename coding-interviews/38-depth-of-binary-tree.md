# 38 二叉树的深度

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

## 题解

```python
def tree_depth(pRoot):
    """ 分治法 """
    if not pRoot:
        return 0
    lval = tree_depth(pRoot.left)
    rval = tree_depth(pRoot.right)
    return max(lval, rval) + 1
```

```python
def tree_depth(pRoot):
    """ 层次遍历 """
    if not pRoot:
        return 0
    q = [pRoot]
    level = 0
    while q:
        sz = len(q)
        while sz:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            sz -= 1
        level += 1
    return level
```

🍥 **考察要点**：二叉树、树的层次遍历、队列、分治法

🍬 **解题思路**：分治法：max(头结点左子树的最大深度，头结点右子树的最大深度) + 1；层次遍历。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)

🍣 **分治法**：求一个规模为n的问题，先求**左边**规模大约为n/2的问题，再求**右边**规模大约为n/2的问题，然后合并左边、右边的解，从而求得最终解。

- 求 `pro(left, right) -> int`
- 先求 `pro(left, (left+right)/2) -> lval`
- 再求 `pro((left+right)/2, right) -> rval`
- `merge(lval, rval) -> result`
