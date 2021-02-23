# 26 二叉搜索树与双向链表

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

## 题解

```python
class Solution(object):
    """ 在牛客网通不过，运行超时 """
    def tree_to_doubly_list(self, root):
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
```

```python
class Solution(object):
    def convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 左子树：找其右子树中最右结点，即根左
        self.convert(pRootOfTree.left)
        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
        # 右子树：找其左子树中最左结点，即根右
        self.convert(pRootOfTree.right)
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giq7d223jnj30nk0hitbu.jpg)

🍥 **考察要点**：二叉搜索树、递归、分治、中序遍历、双向链表

🍬 **解题思路**：二叉搜索树的**中序遍历**为**递增序列**。算法流程如下👇：

1. **终止条件**：当结点 *cur* 为空，直接返回；
2. 递归左子树，即 `dfs(cur.left)`;
3. **构建链表**：
   1. 当 **pre 为空**时，表示正在访问链表头结点，记为 *head*;
   2. 当 **pre 不为空**时，修改双向结点引用，即 *pre.right = cur, cur.left = pre*;
   3. **保存 cur**, 更新 *pre = cur*, 即结点 *cur* 是后继结点的 *pre*.
4. 递归右子树，即 `dfs(cur.right)`.

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
