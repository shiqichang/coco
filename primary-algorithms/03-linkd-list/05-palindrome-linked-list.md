# 05 回文链表

> 🌈 **初级算法系列之链表**
>
> 你的无畏源于无知。

## 题目描述

请判断一个链表是否为回文链表。

### 示例1

> 输入: 1->2
> 输出: false

### 示例2

> 输入: 1->2->2->1
> 输出: true

### 进阶

你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

## 题解

```python
def is_palindrome_(head):
    """ 利用数组 """
    if not (head and head.next):
        return True
    arr, i = [], 0
    while head:
        _, head = arr.append(head.val), head.next
    j = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        i, j = i + 1, j - 1
    return True
```

```python
def is_palindrome_(head):
    """ 双指针➕反转 """
    if not (head and head.next):
        return True
    p = ListNode(-1)
    p.next, slow, fast = head, p, p
    # 快慢指针不断迭代，找到中间结点
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    cur, pre = slow.next, None
    slow.next = None
    # 将链表一分为二后，反转链表后半部分
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    a, b = p.next, pre
    # 将链表前半部分和反转的后半部分对比
    while b:
        if a.val != b.val:
            return False
        a, b = a.next, b.next
    return True
```

🍥 **考察要点**：反转、双指针

🍬 **解题思路**：利用额外的数组，空间复杂度为 O(n); 反转➕双指针。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
