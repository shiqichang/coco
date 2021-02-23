# 31 整数中1出现的次数(从1到n整数中1出现的次数)

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

## 题解

```python
def number_of_between1_and_n(n):
    digit, res = 1, 0
    high, cur, low = n // 10, n % 10, 0
    while high != 0 or cur != 0:
        if cur == 0:
            res += high * digit
        elif cur == 1:
            res += high * digit + low + 1
        else:
            res += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    return res
```

🍥 **考察要点**：数学、递推

🍬 **解题思路**：求 1~n 的个位、十位、百位、...的 1 出现次数相加。设 `n` 为 `x` 位数：

- `ni` 称为 **当前位**  *cur*,  `ni-1ni-2...n2n1` 称为 **低位** *low*, `nxnx-1...ni+2ni+1` 称为 **高位** *high*, `10^i` 称为 **位因子** *digit*.
- 某位中 1 出现次数：
  - `cur == 0` => `high * digit`
  - `cur == 1` -> `high * digit + low + 1`
  - `cur >= 2` -> `high * digit + digit`

🍉 **时间复杂度**：O(logn)

🍭 **空间复杂度**：O(1)
