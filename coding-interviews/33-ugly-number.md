# 33 丑数

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

## 题解

```python
def get_ugly_number(n):
    if n == 0:
        return 0
    dp, a, b, c = [1] * n, 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            a += 1
        if dp[i] == n3:
            b += 1
        if dp[i] == n5:
            c += 1
    return dp[-1]
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1girbgtavwpj30m00iewh5.jpg)

🍥 **考察要点**：动态规划、数学、二分
🍬 **解题思路**：*丑数 = 某较小丑数 x 某因子*。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
