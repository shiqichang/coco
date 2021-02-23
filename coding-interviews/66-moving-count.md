# 66 机器人的运动范围

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

## 题解

```python
def moving_count(threshold, rows, cols):
    def cal_sum(tmp):
        """ 数位之和计算 """
        s = 0
        while tmp != 0:
            s += tmp % 10
            tmp //= 10
        return s

    num = 0
    for i in range(rows):
        for j in range(cols):
            if cal_sum(i) + cal_sum(j) <= threshold:
                num += 1
            elif rows == 1 or cols == 1:
                return num
    return num
```

```python
def moving_count(k, m, n):
    """ 深度优先遍历 """
    def dfs(i, j, si, sj):
        if i >= m or j >= n or k < si + sj or (i, j) in visited:
            return 0
        visited.add((i, j))
        return 1 + dfs(i+1, j, si+1 if (i+1) % 10 else si-8, sj) + dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj-8)
    
    visited = set()
    return dfs(0, 0, 0, 0)
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giuzu5s3szj315o0ls42y.jpg)

```python
def moving_count(k, m, n):
    """ 广度优先遍历 """
    queue, visited = [(0, 0, 0, 0)], set()
    while queue:
        i, j, si, sj = queue.pop(0)
        if i >= m or j >= n or k < si + sj or (i, j) in visited:
            continue
        visited.add((i, j))
        queue.append((i+1, j, si+1 if (i+1) % 10 else si-8, sj))
        queue.append((i, j+1, si, sj+1 if (j+1) % 10 else sj-8))
    return len(visited)
```

![2](https://tva1.sinaimg.cn/large/007S8ZIlly1giuzvmy7kpj31560miwhb.jpg)

🍥 **考察要点**：DFS、BFS

🍬 **解题思路**：深度优先遍历；广度优先遍历。

🍦 **数位和增量公式**：当 `(x+1) % 10 == 0` 时，`sx+1 = sx - 8`; 反之，`sx+1 = sx + 1`.

![3](https://tva1.sinaimg.cn/large/007S8ZIlly1giuzkdawapj314w0o2n5s.jpg)

🍉 **时间复杂度**：O(mn)

🍭 **空间复杂度**：O(mn)
