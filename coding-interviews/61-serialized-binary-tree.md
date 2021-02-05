# 61 序列化二叉树

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现两个函数，分别用来序列化和反序列化二叉树。

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树

## 题解

```python
# 深度优先➕递归
def serialize(root):
    def dfs(node):
        if node:
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        else:
            vals.append('#')
    vals = []
    dfs(root)
    return ','.join(vals)


def deserialize(s):
    def dfs():
        v = next(vals)
        if v == '#':
            return None
        node = TreeNode(int(v))
        node.left = dfs()
        node.right = dfs()
        return node
    vals = iter(s.split(','))
    return dfs()
```

```python
# 广度优先➕队列
def serialize(root):
    res = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            res.append(str(node.val))
        else:
            res.append('#')
    return ','.join(res)


def deserialize(s):
    parts = s.split(',')
    idx = 0
    val = parts[idx]
    if val == '#':
        return None
    root = TreeNode(int(val))
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        idx += 1
        val = parts[idx]
        if val != '#':
            node.left = left = TreeNode(int(val))
            queue.append(left)
        idx += 1
        val = parts[idx]
        if val != '#':
            node.right = right = TreeNode(int(val))
            queue.append(right)
    return root
```

🍥 **考察要点**：二叉树、先序遍历、层序遍历
🍬 **解题思路**：深度优先➕递归；广度优先➕队列。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
