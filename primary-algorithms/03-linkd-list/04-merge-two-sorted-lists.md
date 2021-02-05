# 04 合并两个有序链表

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

### 示例

> 输入：1->2->4, 1->3->4
> 输出：1->1->2->3->4->4

## 题解

```python
def merge_two_lists(l1, l2):
    """ 递归 """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
```

```python
def merge_two_lists(l1, l2):
    """ 迭代 """
    pre_head = ListNode(-1)  # 哨兵结点
    prev = pre_head  # 维护一个 prev 指针
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
        
    # 合并后 l1 和 l2 最多只有一个还未被合并完，直接将链表末尾指向未合并完的链表
    prev.next = l1 if l1 is not None else l2
    return pre_head.next
```

🍥 **考察要点**：递归、迭代
🍬 **解题思路**：递归，空间复杂度为 O(n+m); 迭代。

🍉 **时间复杂度**：O(n+m)
🍭 **空间复杂度**：O(1)
