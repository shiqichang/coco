# 01 反转字符串

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

### 示例1

> 输入：["h","e","l","l","o"]
> 输出：["o","l","l","e","h"]

### 示例2

> 输入：["H","a","n","n","a","h"]
> 输出：["h","a","n","n","a","H"]

## 题解

```python
def reverse_string(s):
    # s[:] = s[::-1]
    s.reverse()
```

```python
def reverse_string(s):
    """ 递归 """
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
            
    helper(0, len(s) - 1)
```

```python
def reverse_string(s):
    """ 双指针法 """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
```

🍥 **考察要点**：递归、双指针

🍬 **解题思路**：递归，空间复杂度为 O(n)；双指针法。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
