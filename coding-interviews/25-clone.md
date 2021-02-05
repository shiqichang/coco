# 25 复杂链表的复制

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

## 题解

```python
import copy

def clone(pHead):
    return copy.deepcopy(pHead)  # 深拷贝
```

```python
def copy_random_list(head):
    def dfs(head):
        """ 深度优先遍历(DFS) """
        if not head:
            return
        if head in visited:
            return visited[head]
        copy = RandomListNode(head.label)
        visited[head] = copy
        copy.next = dfs(head.next)
        copy.random = dfs(head.random)
        return copy
    visited = {}
    return dfs(head)
```

```python
def copy_random_list(head):
    def bfs(head):
        """ 广度优先遍历(BFS) """
        if not head:
            return head
        clone = RandomListNode(head.label)
        queue = deque()
        queue.append(head)
        visited[head] = clone
        while queue:
            tmp = queue.pop()
            if tmp.next and tmp.next not in visited:
                visited[tmp.next] = RandomListNode(tmp.next.label)
                queue.append(tmp.next)
            if tmp.random and tmp.random not in visited:
                visited[tmp.random] = RandomListNode(tmp.random.label)
                queue.append(tmp.random)
            visited[tmp].next = visited.get(tmp.next)
            visited[tmp].random = visited.get(tmp.random)
        return clone
    visited = {}
    return bfs(head)
```

```python
def copy_random_list(head):
    """ 迭代 """
    visited = {}

    def get_clone_node(node):
        if not node:
            return
        if node not in visited:
            visited[node] = RandomListNode(node.label)
        return visited[node]

    if not head:
        return head
    old_head = head
    new_head = RandomListNode(old_head.label)
    visited[old_head] = new_head

    while old_head:
        new_head.random = get_clone_node(old_head.random)
        new_head.next = get_clone_node(old_head.next)

        old_head = old_head.next
        new_head = new_head.next
    return visited[head]
```

```python
def copy_random_list(head):
    """ 迭代优化 """
    if not head:
        return head
    cur = head
    while cur:
        new_node = RandomListNode(cur.label)  # 复制结点
        new_node.next = cur.next
        cur.next = new_node  # 复制结点在 cur 后面
        cur = new_node.next  # 移动到下一个结点

    cur = head
    while cur:
        # 复制结点的 random 结点 = 当前结点的 random 结点的下一个结点
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    cur_old_list = head  # 将两个链表分开
    cur_new_list = head.next
    new_head = head.next
    while cur_old_list:
        cur_old_list.next = cur_old_list.next.next
        cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
        cur_old_list = cur_old_list.next
        cur_new_list = cur_new_list.next
    return new_head
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gimshk3wuij30pc0ckgoo.jpg)

🍥 **考察要点**：链表、DFS、BFS、递归、迭代
🍬 **解题思路**：**图**的基本单元是**顶点**，顶点之间的关联成为**边**。题中的链表可以看成一个图。

- **深度优先搜索**：Depth First Search, DFS
  - 从头结点 `head` 开始拷贝；如果结点已被拷贝，则不需要重复拷贝，否则创建一个新的结点拷贝，并将拷贝过的结点保存在哈希表中，格式 `{原结点：拷贝结点}`；使用递归拷贝所有的 `next` 结点，再递归拷贝所有的 `random` 结点。
- **广度优先搜索**：Breadth First Search, BFS
  - 创建哈希表保存已拷贝结点；创建队列并将头结点入队；当队列不为空，弹出一个结点，若该结点的 `next` 结点未被拷贝，则拷贝并加入队列，同理 `random` 结点。
- **迭代优化**：将链表扩展，在每个链表结点的旁边拷贝，`A->B->C` 变成 `A->A'->B->B'->C->C'`，然后将拷贝的结点分离出来。此时**空间复杂度**为 O(1).

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
