# 15 反转链表

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个链表，反转链表后，输出新链表的表头。

## 题解

```python
def reverse_list(pHead):
    """ 构建链表 """
    if not pHead:
        return
    v = list()
    while pHead:
        v.append(pHead)
        pHead = pHead.next
    v = v[::-1]
    head = v[0]
    cur = head
    for i in range(1, len(v)):
        cur.next = v[i]
        cur = cur.next
    cur.next = None
    return head
```

```python
def reverse_list(pHead):
    """ 3个指针 """
    pre, cur, nex = None, pHead, None
    while cur:
        nex = cur.next
        cur.next = pre
        pre, cur = cur, nex
    return pre
```

🍥 **考察要点**：单链表
🍬 **解题思路**：**3个指针**解法。

- 构建链表：用一个临时容器存储单链表的指针，再构建一个新链表。这种情况的**空间复杂度**为 O(n).
- **3个指针**：循环执行 `nex = cur.next`, `cur.next = pre`, `pre, cur = cur, nex`. 当 `cur` 为空时结束循环。结果返回 `pre`.
  - `pre` 指针指向已反转好的链表的最后一个结点
  - `cur` 指针指向待反转链表的第一个结点
  - `nex` 指针指向待反转链表的第二个结点，目的是保存链表。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
