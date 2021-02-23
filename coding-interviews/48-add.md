# 48 不用加减乘除做加法

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

## 题解

```python
def add(num1, num2):
    x = 0xffffffff
    num1, num2 = num1 & x, num2 & x
    while num2 != 0:
        num1, num2 = num1 ^ num2, (num1 & num2) << 1 & x
    # 查看符号位，正数则直接返回，负数则返回 ~(a^0xffffffff) ~ 表示按位取反
    return num1 if num1 <= 0x7fffffff else -(num1 ^ x)
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gisl65jwqjj316i0a2wf1.jpg)

🍥 **考察要点**：位运算

🍬 **解题思路**：**无进位和**与**异或运算**规律相同，**进位**与**与运算**规律相同（并需左移一位）。故 `n = a^b, c  = (a&b) << 1`.

- *(和 s) = (非进位和 n) + (进位 c)*, 循环求 `n` 和 `c`, 直到进位 `c = 0`, 此时 `s = n`. 返回 `n` 即可。

🍉 **时间复杂度**：O(1)

🍭 **空间复杂度**：O(1)
