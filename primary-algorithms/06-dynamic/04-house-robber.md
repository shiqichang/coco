# 04 打家劫舍

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。
给定一个代表每个房屋存放金额的非负整数数组，计算你 **不触动警报装置的情况下**，一夜之内能够偷窃到的最高金额。

### 示例1

> 输入：[1,2,3,1]
> 输出：4
> 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
> 偷窃到的最高金额 = 1 + 3 = 4 。

### 示例2

> 输入：[2,7,9,3,1]
> 输出：12
> 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
> 偷窃到的最高金额 = 2 + 9 + 1 = 12 。

### 提示

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## 题解

```python
def rob(nums):
    """ 动态规划 """
    if not nums:
        return 0
    size = len(nums)
    if size == 1:
        return nums[0]
    dp = [0] * size
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, size):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[size - 1]
```

```python
def rob(nums):
    """ 动态规划➕滚动数组 """
    if not nums:
        return 0
    size = len(nums)
    if size == 1:
        return nums[0]
    first, second = nums[0], max(nums[0], nums[1])
    for i in range(2, size):
        first, second = second, max(first + nums[i], second)
    return second
```

🍥 **考察要点**：动态规划

🍬 **解题思路**：动态规划➕滚动数组。

- **状态转移方程**：*dp[i] = max(dp[i-2] + numi[i], dp[i-1])*.
- **边界条件**：*dp[0] = nums[0]*, *dp[1] = max(nums[0], nums[1])*.

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
