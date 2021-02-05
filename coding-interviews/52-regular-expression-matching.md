# 52 正则表达式匹配

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请实现一个函数用来匹配包括 `.` 和 `*` 的正则表达式。模式中的字符`.` 表示任意一个字符，而 `*` 表示它前面的字符可以出现任意次（包含0次）。匹配是指字符串的所有字符匹配整个模式。例如，字符串 `aaa` 与模式 `a.a` 和 `ab*ac*a` 匹配，但与 `aa.a` 和 `ab*a` 均不匹配。

## 题解

```python
def is_match(s, p):
    """ 回溯 """
    if not p:
        return not s  # 边界条件
    # 第一个字母是否匹配
    first_match = bool(s and p[0] in {s[0], '.'})
    # 如果 p 第二个字母是 *
    if len(p) >= 2 and p[1] == "*":
        return is_match(s, p[2:]) or first_match and is_match(s[1:], p)
    else:
        return first_match and is_match(s[1:], p[1:])
```

```python
def is_match(s, p):
    """ 动态规划 """
    # 边界条件，考虑 s 或 p 分别为空的情况
    if not p:
        return not s
    if not s and len(p) == 1:
        return False

    m, n = len(s) + 1, len(p) + 1
    dp = [[False for _ in range(n)] for _ in range(m)]
    # 初始状态
    dp[0][0] = True
    dp[0][1] = False

    for c in range(2, n):
        j = c - 1
        if p[j] == '*':
            dp[0][c] = dp[0][c-2]

    for r in range(1, m):
        i = r - 1
        for c in range(1, n):
            j = c - 1
            if s[i] == p[j] or p[j] == '.':
                dp[r][c] = dp[r-1][c-1]
            elif p[j] == '*':  # '*' 前面的字符匹配 s[i] 或 '.'
                if p[j-1] == s[i] or p[j-1] == '.':
                    dp[r][c] = dp[r-1][c] or dp[r][c-2]
                else:
                    dp[r][c] = dp[r][c-2]
            else:
                dp[r][c] = False
    return dp[m-1][n-1]
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gitnca0hhjj30r20c6758.jpg)

🍥 **考察要点**：字符串、动态规划、递归
🍬 **解题思路**：回溯；动态规划。

- **回溯**：考虑只有 `.` 的情况，从左到右依次判断 `s[i]` 与 `p[i]` 是否匹配。
  - 若有 `*`:  `*` 代表0个前面的元素，则直接忽略 `p` 的 `a*`；`*` 代表匹配一个或多个前面的元素，则忽略 `s` 的第一个元素。
- **动态规划**：`dp[i][j]` 表示 `s` 的前 `i` 项和 `p` 的前 `j` 项是否匹配。以下是所有能匹配的情况👇
  - `s[i] == p[j] or p[j] == '.'`
  - `p[j] == '*'` -> `p[j-1] != s[i]` or `p[j-1] == s[i] or p[j-1] == '.'`
  - 沿着匹配串和字符串构成矩阵的对角线传递状态

🍉 **时间复杂度**：O(mn)
🍭 **空间复杂度**：O(mn)
