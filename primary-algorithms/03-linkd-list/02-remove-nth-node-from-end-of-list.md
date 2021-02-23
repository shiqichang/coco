# 02 删除链表中的倒数第N个结点

> 🌈 **初级算法系列之链表**
>
> 你的无畏源于无知。

## 题目描述

给定一个链表，删除链表的倒数第 *n* 个节点，并且返回链表的头结点。

### 示例

> 给定一个链表: 1->2->3->4->5, 和 n = 2.
>
> 当删除了倒数第二个节点后，链表变为 1->2->3->5.

### 说明

给定的 *n* 保证是有效的。

### 进阶

你能尝试使用一趟扫描实现吗？

## 题解

```python
def remove_nth_from_end(head, n):
    """ 两次遍历 """
    dummy = ListNode(0)  # 哑结点
    dummy.next = head
    length = 0
    first = head
    # 第一次遍历，求出链表的长度 L
    while first:
        length += 1
        first = first.next
    length -= n
    first = dummy  # 设置一个指向哑结点对指针
    # 移动它遍历链表，直到它到达第 L-n 个结点
    while length > 0:
        length -= 1
        first = first.next
    first.next = first.next.next  # 把第 L-n 个结点的 next 指针重新链接到第 L-n+2 个结点
    return dummy.next
```

```python
def remove_nth_from_end(head, n):
    """ 两次遍历 """
    dummy = ListNode(0)  # 哑结点
    dummy.next = head
    first, second = dummy, dummy
    # Advances first pointer so that the gap between first and second is n nodes apart
    for i in range(1, n+2):
        first = first.next
    # Move first to the end, maintaining the gap
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
```

🍥 **考察要点**：双指针

🍬 **解题思路**：两次遍历，设置一个*哑结点*；一次遍历➕双指针。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
