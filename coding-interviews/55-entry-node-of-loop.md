# 55 链表中环的入口结点

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

## 题解

```python
def entry_node_of_loop(pHead):
    """ 哈希法 """
    visited = set()
    node = pHead
    while node:
        if node in visited:
            return node
        else:
            visited.add(node)
            node = node.next
    return None
```

```python
def entry_node_of_loop(pHead):
    fast, slow = pHead, pHead
    # 快慢指针相遇点
    while True:
        if not (fast and fast.next):
            return 
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            break
    # 环的头结点
    fast = pHead
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast
```

🍥 **考察要点**：单链表、哈希、双指针

🍬 **解题思路**：哈希法；**Floyd 算法**。

- 哈希法：用一个 `set` 保存已经访问过的结点。遍历整个列表并返回第一个出现重复的结点。时间/空间复杂度均为 O(n);
- **Floyd 算法**：每次移动慢指针一步，快指针两步。若快慢指针指向了同一结点，就返回他它。
  - `2 * distance(tortoise) == distance(hare)` -> `2(F+a) = F+a+b+a` -> `F=b`

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
