# 12 数值的整数次方

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。保证base和exponent不同时为0

## 题解

```python
class Solution:
    def Power(self, base, exponent):
        """ 非递归的快速幂 """
        # write code here
        # return pow(base, exponent)
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        x = base
        ret = 1.0
        while exponent:
            if exponent & 1:
                ret *= x
            x *= x
            exponent >>= 1
        return ret
```

```python
class Solution:
    def q_power(self, base, exponent):
        """ 递归的快速幂 """
        # write code here
        if exponent == 0:
            return 1.0
        ret = self.q_power(base, exponent // 2)
        if exponent & 1:
            return ret * ret * base
        else:
            return ret * ret
        
    def Power(self, base, exponent):
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
            
        return self.q_power(base, exponent)
```

🍥 **考察要点**：数学、递归、快速幂

🍬 **解题思路**：

- **非递归的快速幂**：遍历 exponent 的二进制位，是1就乘进结果。
  - e.g `x^6 = x^(0*2^0 + 1*2^1 + 1*2^2) = x^0 * x^(1*2^1) * x^(1*2^2)`
- **递归的快速幂**：n 为偶数，`x^n = (x^(n/2))^2`; n 为奇数，`x^n = (x^(n/2))^2 * x`
  - e.g `x^8 = (x^4)^2`, `x^7 = (x^3)^2 * x`

🍉 **时间复杂度**：O(logn)

🍭 **空间复杂度**：O(1)
