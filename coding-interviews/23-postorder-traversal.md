# 23 二叉搜索树的后序遍历序列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。

## 题解

```python
def verify_sequence_of_bst(sequence):
    """ 递归分治 """
    if not sequence:
        return False
    
    def recur(i, j):
        if i >= j:
            return True
        p = i
        while sequence[p] < sequence[j]:
            p += 1
        m = p
        while sequence[p] > sequence[j]:
            p += 1
        return p == j and recur(i, m - 1) and recur(m, j - 1)

    return recur(0, len(sequence) - 1)
```

```python
def verify_sequence_of_bst(sequence):
    """ 单调辅助栈 """
    stack, root = [], float("+inf")
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] > root:
            return False
        while stack and sequence[i] < stack[-1]:
            root = stack.pop()
        stack.append(sequence[i])
    return True
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gilnwsvtivj30ls0gctaf.jpg)

*二叉搜索树 (Binary Search Tree, BST): 左孩子 < 根结点 < 右孩子，它的左孩子和右孩子也都是 BST.*

🍥 **考察要点**：二叉搜索树、树的后序遍历、栈

🍬 **解题思路**：递归分治；辅助单调栈。

- **递归分治**：时间复杂度为 `O(n^2)`
  - **划分左右子树**，寻找**第一个大于根结点**的结点，索引记为 `m`, 可以得出左子树区间 `[i, m-1]`, 右子树区间 `[m, j-1]`, 根结点索引为 `j`.
  - **判断是否为二叉搜索树**：左子树区间 `[i, m-1]` 内所有的结点 `< postorder[j]`, 右子树区间 `[m, j-1]` 内所有的结点 `> postorder[j]`. 遇到 `>=` 的结点就跳出，此时通过 `p==j` 判断是否为二叉搜索树。
- **辅助单调栈**：后序遍历倒序为**根右左** `[rn,rn-1,...,r1]`
  - 当 `ri > ri+1` 时，`ri` 一定是 `ri+1` 的右子结点
  - 当 `ri < ri+1` 时，`ri` 一定是某结点 `root` 的左子结点，且 `root` 为 `ri+1, ri+2,...,rn` 中值大于且最接近 `ri` 的结点。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
