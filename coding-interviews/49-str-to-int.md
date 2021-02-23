# 49 把字符串转换成整数

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0.

### 输入描述

> 输入一个字符串,包括数字字母符号,可以为空

### 示例1

输入

> +2147483647
> 1a33

输出

> 2147483647
> 0

## 题解

```python
def str2int(s):
    s = s.strip()  # 删除首尾空格
    if not s:
        return 0  # 字符串为空则直接返回
    res, i, sign = 0, 1, 1
    int_max, int_min, bndry = 2**31-1, -2**31, 2**31//10
    if s[0] == '-':
        sign = -1  # 保存负号
    elif s[0] != '+':
        i = 0  # 若无符号位，则需从 i=0 开始数字拼接
    for c in s[i:]:
        if not '0' <= c <= '9':
            return 0  # 遇到非数字的字符则跳出
        if res > bndry or (res == bndry and c > '7'):
            return int_max if sign == 1 else int_min  # 数字越界处理
        res = 10 * res + ord(c) - ord('0')  # 数字拼接
    return sign * res
```

```python
def str2int(s):
    """ 不使用 strip() 方法，空间复杂度为 O(1) """
    if not s:
        return 0  # 空字符串，提前返回
    res, i, sign, length = 0, 0, 1, len(s)
    int_max, int_min, bndry = 2**31-1, -2**31, 2**31//10
    while s[i] == ' ':
        i += 1
        if i == length:
            return 0  # 字符串全为空格，提前返回
    if s[i] == '-':
        sign = -1
    elif s[i] in '+-':
        i += 1
    for c in s[i:]:
        if not '0' <= c <= '9':
            return 0  # 遇到非数字的字符则跳出
        if res > bndry or (res == bndry and c > '7'):
            return int_max if sign == 1 else int_min  # 数字越界处理
        res = 10 * res + ord(c) - ord('0')  # 数字拼接
    return sign * res
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gismkv1r2aj30n00e2dhx.jpg)

![2](https://tva1.sinaimg.cn/large/007S8ZIlly1gismqiruk1j30ku0g2tba.jpg)

🍥 **考察要点**：字符串、数字越界处理

🍬 **解题思路**：考虑4种字符(*首部空格；符号位；非数字字符；数字字符*)。要求返回的数值范围应在 `[-2^31, 2^31-1]`

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
