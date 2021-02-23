# 16 合并两个排序的链表

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

## 题解

```python
def Merge(pHead1, pHead2):
    """ 迭代版本 """
    vhead = ListNode(-1)
    cur = vhead
    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            cur.next = pHead1
            pHead1 = pHead1.next
        else:
            cur.next = pHead2
            pHead2 = pHead2.next
        cur = cur.next
    cur.next = pHead1 if pHead1 else pHead2
    return vhead.next
```

```python
def Merge(pHead1, pHead2):
    """ 递归版本 """
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    if pHead1.val <= pHead2.val:
        pHead1.next = Merge(pHead1.next, pHead2)
        return pHead1
    else:
        pHead2.next = Merge(pHead1, pHead2.next)
        return pHead2
```

🍦 **技巧**：一般创建单链表，都会设一个虚拟头节点，也叫**哨兵**，这样每一个结点都有一个前驱结点。

🍥 **考察要点**：单链表、递归

🍬 **解题思路**：迭代或递归解法。

- 迭代版本：定义 `cur` 指向新链表的头结点。若 `pHead1.val <= pHead2.val`, 则 `cur.next = pHead1; pHead1 = pHead1.next; cur = cur.next`.
- 递归版本：若 `pHead1` 所指的结点值小于等于 `pHead2` 所指的结点值，则 `pHead1` 后续结点和 `pHead2` 结点继续递归。此时**空间复杂度**为 O(m+n).

🍉 **时间复杂度**：O(m+n)

🍭 **空间复杂度**：O(1)
