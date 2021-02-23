# 67 剪绳子

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积18。

### 输入描述

> 输入一个数n，意义见题面。（2 <= n <= 60）

### 输出描述

> 输出答案。

### 示例1

输入

> 8

输出

> 18

## 题解

```python
def cutRope(number):
    a = [0] * 60
    a[1] = 1
    a[2] = 2
    a[3] = 3
    for i in range(4, number + 1):
        max = 0
        for j in range(1, int(i // 2) + 1):
            a[i] = a[j] * a[i - j]
            if max < a[i]:
                max = a[i]
            a[i] = max
    return a[number]
```

```python
def cutRope(n):
    """ 数学推导 """
    if n <= 3:
        return n-1
    a, b = n // 3, n % 3
    if b == 0:
        return int(3**a)
    if b == 1:
        return int((3**(a-1)) * 4)
    return int((3**a) * 2)
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giv034r75wj30re0kqjsl.jpg)

🍥 **考察要点**：数学推导、贪心算法

🍬 **解题思路**：数学推导；贪心思路。

- **数学推导**： 尽可能将绳子以长度3等分为多段。**切分规则：最优为3，次优为2，最差为1。**
  - 当 `n <= 3` 时，剪出一段，返回 `n-1`;
  - 当 `n > 3` 时，分三种情况：
    - 当 `b = 0`, 直接返回 `3^a`;
    - 当 `b = 1`, 则返回 `(3^(a-1))*4`;
    - 当 `b = 2`, 就返回 `(3^a)*2`.
- **贪心思路**：

![2](https://tva1.sinaimg.cn/large/007S8ZIlly1giv0c1goujj31620fyjtr.jpg)

🍉 **时间复杂度**：O(1)

🍭 **空间复杂度**：O(1)
