# 01 二叉树的最大深度

> 🌈 **初级算法系列之树**
>
> 你的无畏源于无知。

## 题目描述

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
**说明:** 叶子节点是指没有子节点的节点。

### 示例

> 给定二叉树 `[3,9,20,null,null,15,7]`，
>
> ```shell
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> 返回它的最大深度 3 。

## 题解

```python
def max_depth(root):
    """ 递归 """
    if root is None:
        return 0
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    return max(left_height, right_height) + 1
```

```python
def max_depth(root):
    """ 广度优先搜索(BFS) """
    if root is None:
        return 0
    queue = [root]
    ans = 0
    while queue:
        size = len(queue)
        while size > 0:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            size -= 1
        ans += 1
    
    return ans
```

🍥 **考察要点**：递归、广度优先搜索(BFS)

🍬 **解题思路**：递归➕深度优先搜索(DFS)；广度优先搜索(BFS).

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
