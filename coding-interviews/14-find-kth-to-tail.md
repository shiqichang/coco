# 14 链表中倒数第k个结点

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入一个链表，输出该链表中倒数第k个结点。

## 题解

```python
def find_kth_to_tail(head, k):
    """ 普通解法 """
    if not head or k <= 0:
        return
    n = 0
    cur = head
    while cur:
        cur = cur.next
        n += 1
    if n < k:
        return
    n -= k
    while n:
        head = head.next
        n -= 1
    return head
```

```python
def find_kth_to_tail(head, k):
    """ 快慢指针解法 """
    if not head or k <= 0:
        return
    slow, fast = head, head
    while k:
        if fast:
            fast = fast.next
        else:
            return
        k -= 1
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
```

🍥 **考察要点**：链表、链表的快慢指针
🍬 **解题思路**：快慢指针解法。

- 普通解法：求出链表的总长度；求倒数第 `k` 个，那么正数是从头结点开始往后推 `n-k` 个。此方法需要遍历链表2次。
- **快慢指针**：快指针先往前走 `k` 步，然后快慢一起走，当快指针指向空结点时，慢指针就是倒数第 `k` 个结点。
- 边界条件：`k <= 0` ; 头结点为空；链表总长度小于 `k`.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
