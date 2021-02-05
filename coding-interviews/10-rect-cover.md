# 10 矩形覆盖

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

我们可以用 `2*1` 的小矩形横着或者竖着去覆盖更大的矩形。请问用n个 `2*1` 的小矩形无重叠地覆盖一个 `2*n` 的大矩形，总共有多少种方法？比如 n=3 时，2 * 3的矩形块有3种覆盖方法：

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gijf5qc6euj310a0p4407.jpg)

## 题解

```python
def rect_cover(number):
    if number == 0 or number == 1 or number == 2:
        return number

    i, j = 1, 2
    for _ in range(3, number + 1):
        i, j = j, i + j
    return j
```

分析从 `n=3` 到 `n=4`:

- 直接在 `n=3` 的情况下，在后面添加一个竖着的；
- 将横着的添加到 `n=2` 的情况上。
- 由👆可得：`f(n) = f(n-1) + f(n-2)`, 初始条件 `f(1) = 1, f(2) = 2`.

🍥 **考察要点**：递归、记忆递归、动态规划、递推
🍬 **解题思路**：同**跳台阶**解法。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)