# 04 罗马数字转整数

> 🌈 **初级算法系列之数学**
>
> 你的无畏源于无知。

## 题目描述

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```shell
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 2 写做 `II` ，即为两个并列的 1。12 写做 `XII` ，即为 `X` + `II` 。 27 写做 `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

### 示例1

> 输入: "III"
> 输出: 3

### 示例2

> 输入: "IV"
> 输出: 4

### 示例3

> 输入: "IX"
> 输出: 9

### 示例4

> 输入: "LVIII"
> 输出: 58
> 解释: L = 50, V= 5, III = 3.

### 示例5

> 输入: "MCMXCIV"
> 输出: 1994
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

### 提示

- 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
- IC 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
- 关于罗马数字的详尽书写规则，可以参考 [罗马数字 - Mathematics](https://b2b.partcommunity.com/community/knowledge/zh_CN/detail/10753/罗马数字#knowledge_article)。

## 题解

```python
def roman_to_int(s):
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80,
         'C': 100, 'CD': 300, 'D': 500, 'CM': 800, 'M': 1000}
    return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
```

```python
def roman_to_int(s):
    roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    n = len(s)
    for index in range(n-1):
        if roman2int[s[index]] < roman2int[s[index+1]]:
            res -= roman2int[s[index]]
        else:
            res += roman2int[s[index]]
    return res + roman2int[s[-1]]
```

🍥 **考察要点**：哈希表

🍬 **解题思路**：只有在遇到特殊情况时，两个字符中左边的字符小于右边的字符，且等于右边的字符代表的数减左边字符代表的数。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
