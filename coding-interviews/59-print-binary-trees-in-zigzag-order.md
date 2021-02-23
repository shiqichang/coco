# 59 按之字形顺序打印二叉树

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

## 题解

```python
import collections

def level_order(root):
    """ 层序遍历➕双端队列 """
    if not root:
        return []
    res, deque = [], collections.deque([root])
    while deque:
        tmp = collections.deque()
        for _ in range(len(deque)):
            node = deque.popleft()
            if len(res) % 2:
                tmp.appendleft(node.val)  # 偶数层 -> 队列头部
            else:
                tmp.append(node.val)  # 奇数层 -> 队列尾部
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        res.append(list(tmp))
    return res
```

```python
import collections

def level_order(root):
    """ 层序遍历➕双端队列（奇偶层逻辑分离） """
    if not root:
        return []
    res, deque = [], collections.deque([root])
    while deque:
        tmp = []
        # 打印奇数层
        for _ in range(len(deque)):
            # 从左到右打印
            node = deque.popleft()
            tmp.append(node.val)
            # 从左向右加入下层结点
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        res.append(tmp)
        if not deque:
            break  # 若为空则提前跳出
        # 打印偶数层
        tmp = []
        for _ in range(len(deque)):
            # 从右向左打印
            node = deque.pop()
            tmp.append(node.val)
            # 从右向左加入下层结点
            if node.right:
                deque.appendleft(node.right)
            if node.left:
                deque.appendleft(node.left)
    return res
```

```python
import collections

def level_order(root):
    """ 层序遍历➕倒序 """
    if not root:
        return []
    res, deque = [], collections.deque([root])
    while deque:
        tmp = []
        for _ in range(len(deque)):
            node = deque.popleft()
            tmp.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        res.append(tmp[::-1] if len(res) % 2 else tmp)
    return res
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giumdk3troj30ko0c0jtm.jpg)

🍥 **考察要点**：二叉树、队列、层次遍历

🍬 **解题思路**：打印顺序交替变化。

- 层序遍历➕双端队列：奇数层添加到链表**尾部**，偶数层添加到链表**头部**；
- 层序遍历➕双端队列（奇偶层逻辑分离）：**BFS 循环**，循环打印奇/偶数层；
- 层序遍历➕倒序：**偶数层倒序**。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
