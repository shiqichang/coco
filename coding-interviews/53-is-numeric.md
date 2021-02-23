# 53 表示数值的字符串

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

## 题解

```python
def is_numeric(s):
    try:
        float(s)
        return True
    except:
        return False
```

```python
def is_numeric(s):
    states = [
        {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
        {'d': 2, '.': 4},                  # 1. 'sign' before 'e'
        {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
        {'d': 3, 'e': 5, ' ': 8},          # 3. 'digit' after 'dot'
        {'d': 3},                          # 4. 'digit' after 'dot'('blank' before 'dot')
        {'s': 6, 'd': 7},                  # 5. 'e'
        {'d': 7},                          # 6. 'sign' after 'e'
        {'d': 7, ' ': 8},                  # 7. 'digit' after 'e'
        {' ': 8}                           # 8. end with 'blank'
    ]
    p = 0  # start with state 0
    for c in s:
        if '0' <= c <= '9':  # digit
            t = 'd'
        elif c in '+-':  # sign
            t = 's'
        elif c in 'eE':  # e or E
            t = 'e'
        elif c in '. ':  # dot, blank
            t = c
        else:  # unknown
            t = '?'
        if t not in states[p]:
            return False
        p = states[p][t]
    return p in (2, 3, 7, 8)
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gitofdf0wyj30y00qc101.jpg)

🍥 **考察要点**：字符串、正则表达式

🍬 **解题思路**：**有限状态自动机**。

- 字符类型：空格、数字 `0-9`、正负号 `+-`、小数点 `.`、幂符号 `eE`.
- 合法的**结束状态**有 2, 3, 7, 8.

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
