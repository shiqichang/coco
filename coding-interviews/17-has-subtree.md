# 17 树的子结构

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

## 题解

```python
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.dfs(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
    
    def dfs(self, r1, r2):
        if not r2:
            return True
        if not r1:
            return False
        return r1.val == r2.val and self.dfs(r1.left, r2.left) and self.dfs(r1.right, r2.right)
```

```python
def is_sub_structure(A: TreeNode, B: TreeNode) -> bool:
    def recur(A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return recur(A.left, B.left) and recur(A.right, B.right)
    
    return bool(A and B) and (recur(A, B) or is_sub_structure(A.left, B) or is_sub_structure(A.right, B))
```

🍦 **技巧**：一般返回布尔类型的递归程序，**与**和**或**运算的灵活使用，可以使代码非常简洁。

🍥 **考察要点**：树、递归

🍬 **解题思路**：首先判断树 A 和树 B 的**根结点**是否一样；如果不一样，判断 A 的**左孩子**和 B 的*根结点*是否一样，同理判断 A 的**右孩子**和 B 的根结点是否一样，若都不满足则不包含。

- 若找到 A 中有值和 B 的根结点相同，则比较左右子树是否相同；
- 若 B 为空，则说明包含；A 为空，则说明不包含。

🍉 **时间复杂度**：O(m*n)

- 先序遍历树 A 占用 O(m), 每次调用 `recur(A, B)` 判断占用 O(n).

🍭 **空间复杂度**：O(m)

- 当数 A 和 B 退化到链表，递归调用深度最大。
