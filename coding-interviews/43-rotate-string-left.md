# 43 左旋转字符串

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

## 题解

```python
def left_rotate_string(s, n):
    """ 字符串切片 """  
    return s[n:] + s[:n]
```

```python
def left_rotate_string(s, n):
    """ 列表遍历拼接 """
    res = []
    for i in range(n, n + len(s)):
        res.append(s[i % len(s)])  # 求余运算
    return ''.join(res)
```

```python
def left_rotate_string(s, n):
    """ 字符串遍历拼接 """
    res = ""
    for i in range(n, n + len(s)):
        res += s[i % len(s)]
    return res
```

🍥 **考察要点**：字符串

🍬 **解题思路**：字符串切片；列表遍历拼接；字符串遍历拼接。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
