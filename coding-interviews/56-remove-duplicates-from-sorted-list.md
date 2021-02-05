# 56 删除链表中重复的结点

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表 `1->2->3->3->4->4->5` 处理后为 `1->2->5`

## 题解

```python
def delete_duplication(pHead):
    newhead = ListNode('a')
    newhead.next = pHead
    pre, cur = None, newhead
    while cur:
        pre = cur
        cur = cur.next
        # 判断指针的下一个值是否与当前值相等
        while cur and cur.next and cur.val == cur.next.val:
            t = cur.val
            # 和当前值t相等的结点都被抛弃
            while cur and t == cur.val:
                cur = cur.next
            pre.next = cur
    return newhead.next
```

🍥 **考察要点**：单链表
🍬 **解题思路**：直接删除法。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
