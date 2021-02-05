# 01 爬楼梯

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
**注意：** 给定 *n* 是一个正整数。

### 示例1

> 输入： 2
> 输出： 2
> 解释： 有两种方法可以爬到楼顶。
>
> 1. 1 阶 + 1 阶
> 2. 2 阶

### 示例2

> 输入： 3
> 输出： 3
> 解释： 有三种方法可以爬到楼顶。
>
> 1. 1 阶 + 1 阶 + 1 阶
> 2. 1 阶 + 2 阶
> 3. 2 阶 + 1 阶

## 题解

```python
def climb_stairs(n):
    """ 动态规划 """
    p, q, r = 0, 0, 1
    for i in range(1, n+1):
        p = q
        q = r
        r = p + q
    return r
```

```java
public class Solution {
   // 矩阵快速幂
   public int climbStairs(int n) {
       int[][] q = {{1, 1}, {1, 0}};
       int[][] res = pow(q, n);
       return res[0][0];
   }
   public int[][] pow(int[][] a, int n) {
       int[][] ret = {{1, 0}, {0, 1}};
       while (n > 0) {
           if ((n & 1) == 1) {
               ret = multiply(ret, a);
           }
           n >>= 1;
           a = multiply(a, a);
       }
       return ret;
   }
   public int[][] multiply(int[][] a, int[][] b) {
       int[][] c = new int[2][2];
       for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
               c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
           }
       }
       return c;
   }
}
```

```java
public class Solution {
    // 通项公式 
    public int climbStairs(int n) {
        double sqrt5 = Math.sqrt(5);
        double fibn = Math.pow((1 + sqrt5) / 2, n + 1) - Math.pow((1 - sqrt5) / 2, n + 1);
        return (int)(fibn / sqrt5);
    }
}
```

🍥 **考察要点**：动态规划
🍬 **解题思路**：斐波那契数列。

- **动态规划**：`f(x) = f(x-1) + f(x-2)`
- 其他：**矩阵快速幂**、**通项公式**，时间复杂度为 O(logn)

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
