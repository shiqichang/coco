# 02 替换空格

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为 We%20Are%20Happy。

## 题解

```python
def replace_space(s):
    new_s = list()
    for i in s:
        if i == ' ':
            new_s.extend("%20")
        else:
            new_s.extend(i)
    return "".join(new_s)
```

🍥 **考察要点**：字符串

🍬 **解题思路**：一次遍历，使用新的数组存储。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)

其他方法，使用 **内置函数**  `replace('', '%20')`，或者使用 **正则**  `re.sub('', '%20', s)`.

还有官方解法——**逆向遍历**

```python
def replace_space(s):
    k = len(s)
    n = 0
    for i in s:
        if i == ' ':
            n += 1
    kk = k + 2*n
    ss = ['0']*kk
    i = k - 1
    while i >= 0:
        if s[i] == ' ':
            ss[i+2*n] = '0'
            ss[i-1+2*n] = '2'
            ss[i-2+2*n] = '%'
            i -= 1
            n -= 1
        else:
            ss[i+2*n] = s[i]
            i -= 1
    return ''.join(ss)
```
