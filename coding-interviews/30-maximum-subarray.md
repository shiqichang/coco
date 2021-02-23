# 30 连续子数组的最大和

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

## 题解

```python
def find_greatest_sum_of_subarray(array):
    n = len(array)
    dp = [i for i in array]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + array[i], array[i])
    return max(dp)
```

```python
def find_greatest_sum_of_subarray(array):
    sum = 0
    sum_list = []
    for i in array:
        sum += i
        sum_list.append(sum)
        if sum > 0:
            continue
        else:
            sum = 0
    return max(sum_list)
```

🍥 **考察要点**：数组、动态规划

🍬 **解题思路**：动态规划，当 `i != 0 and dp[i] > 0` 时，`dp[i] = dp[i-1] + p[i]`; 当 `i == 0 or dp[i] < 0` 时，`dp[i] = p[i]`.

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
