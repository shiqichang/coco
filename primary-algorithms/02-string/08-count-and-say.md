# 08 外观数列

> 🌈 **初级算法系列之字符串**
>
> 你的无畏源于无知。

## 题目描述

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

```shell
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

第一项是数字 1
描述前一项，这个数是 1 即 “一个 1 ”，记作 11
描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

### 示例1

> 输入: 1
> 输出: "1"
> 解释：这是一个基本样例。

### 示例2

> 输入: 4
> 输出: "1211"
> 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

## 题解

```python
def count_and_say(n):
    """ 递归 """
    if n == 1:
        return '1'
    s = count_and_say(n-1)

    i, res = 0, ''
    for j, c in enumerate(s):
        if c != s[i]:
            res += str(j - i) + s[i]  # 使用 j-i 统计相同元素的个数
            i = j
    res += str(len(s) - i) + s[-1]  # 统计最后一个元素
    return res
```

```python
def count_and_say(n):
    """ 迭代 """
    res = '1'
    for _ in range(n-1):  # 控制循环次数
        i, tmp = 0, ''
        for j, c in enumerate(res):
            if c != res[i]:
                tmp += str(j - i) + res[i]
                i = j
        res = tmp + str(len(res) - i) + res[-1]
    return res
```

```python
def count_and_say(n):
    """ 正则表达式：提取元素 """
    if n == 1:
        return '1'
    s = count_and_say(n-1)

    p = r'(\d)\1*'
    pattern = re.compile(p)
    res = [_.group() for _ in pattern.finditer(s)]  # 提取结果
    return ''.join(str(len(c)) + c[0] for c in res)  # join 内部的是生成器
```

```python
def count_and_say(n):
    """ 正则表达式：元素替换 """
    res = '1'
    p = r'(\d)\1*'  # \1 是为了引用前面的 \d, 表明 \1 是与 \d 匹配到相同的数字
    pattern = re.compile(p)
    for _ in range(n-1):
        res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)  # 替换
    return res
```

🍥 **考察要点**：双指针、迭代、递归、正则表达式

🍬 **解题思路**：递归；迭代；正则表达式。

- `(\d)\1*` 用来提取连在一起的元素。

🍉 **时间复杂度**：O(n^2)

🍭 **空间复杂度**：O(n)
