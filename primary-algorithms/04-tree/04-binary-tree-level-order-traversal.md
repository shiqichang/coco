# 04 二叉树的层序遍历

> 🌈 **初级算法系列之树**
>
> 你的无畏源于无知。

## 题目描述

给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。

### 示例

> 二叉树：`[3,9,20,null,null,15,7]`,
>
> ```shell
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> 返回其层次遍历结果：
>
> ```shell
> [
>   [3],
>   [9,20],
>   [15,7]
> ]
> ```

## 题解

```python
def level_order(root):
    """ 广度优先遍历➕迭代 """
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        # 获取当前队列的长度，这个长度相当于 当前这一层的结点个数
        size = len(queue)
        tmp = []
        # 将队列中的元素都拿出来，也就是获取这一层的结点，放入到临时 list 中
        # 如果结点的左/右子树不为空，也放入队列中
        for _ in range(size):
            r = queue.pop(0)
            tmp.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        # 将临时 list 加入最终返回结果中
        res.append(tmp)
    return res
```

```python
def level_order(root):
    """ 深度优先遍历➕递归 """
    if not root:
        return []
    res = []
    
    def dfs(index, r):
        # 假设 res 是 [[1], [2,3]], index 是 3, 就再插入一个空 list 放到 res 中
        if len(res) < index:
            res.append([])
        # 将当前结点的值加入到 res 中，index 代表当前层，假设 index 是 3, 结点值是 99
        # res 是 [[1], [2,3], [4]], 加入后 res 变为 [[1], [2,3], [4,99]]
        res[index-1].append(r.val)
        # 递归的处理左子树，右子树，同时将层数 index+1
        if r.left:
            dfs(index+1, r.left)
        if r.right:
            dfs(index+1, r.right)
    dfs(1, root)
    return res
```

🍥 **考察要点**：广度优先遍历、迭代、深度优先遍历、递归

🍬 **解题思路**：广度优先遍历➕迭代；深度优先遍历➕递归，空间复杂度为 O(h), h 为树的高度。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
