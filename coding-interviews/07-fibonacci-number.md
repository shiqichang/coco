# 07 斐波那契数列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。n<=39

## 题解

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    i, j = 0, 1
    for _ in range(2, n + 1):
        i, j = j, i + j
        # j = i + j
        # i = j - i
    return j
```

🍥 **考察要点**：递归、记忆化搜索、动态规划和动态规划的空间优化
🍬 **解题思路**：只存储最近的两个数。`i, j = j, i+j` .

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)

这里使用递归会超时，时间复杂度为 O(2^n^).