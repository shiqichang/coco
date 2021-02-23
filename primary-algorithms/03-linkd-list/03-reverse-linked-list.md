# 03 反转链表

> 🌈 **初级算法系列之链表**
>
> 你的无畏源于无知。

## 题目描述

反转一个单链表。

### 示例

> 输入: 1->2->3->4->5->NULL
> 输出: 5->4->3->2->1->NULL

### 进阶

你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

## 题解

```python
def reverse_list(head):
    """ 双指针迭代 """
    if not head:
        return
    cur = head
    pre = None
    while cur:
        tmp = cur.next  # 记录当前结点的下一个结点
        cur.next = pre  # 将当前结点指向 pre
        pre = cur  # pre 结点前进一位
        cur = tmp  # cur 结点前进一位
    return pre
```

```python
def reverse_list(head):
    """ 递归 """
    # 递归终止条件是当前为空，或者下一个结点为空
    if head is None or head.next is None:
        return head
    cur = reverse_list(head.next)  # 这里的 cur 是最后一个结点
    head.next.next = head
    head.next = None  # 防止链表循环，将 head.next 设置为空
    # 每层递归函数都返回 cur，也就是最后一个结点
    return cur
```

🍥 **考察要点**：迭代、递归

🍬 **解题思路**：双指针迭代；递归，空间复杂度为 O(n).

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
