# 02 计数质数

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

统计所有小于非负整数 *n* 的质数的数量。

### 示例

> 输入: 10
> 输出: 4
> 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7。

## 题解

```python
def count_primes(n):
    is_prime = [True] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    count = 0
    for i in range(2, n):
        if is_prime[i]:
            count += 1
    return count
```

🍥 **考察要点**：贪心算法
🍬 **解题思路**：Sieve of Eratosthenes 算法。

🍉 **时间复杂度**：O(n * loglogn)
🍭 **空间复杂度**：O(n)
