# 40 数组中只出现一次的数字

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

## 题解

```python
def find_nums_appear_once(array):
    dic = collections.Counter(array)
    res = []
    for k, v in dic.items():
        if v == 1:
            res.append(k)
    return res
```

```python
def find_nums_appear_once(array):
    res = 0
    x, y = 0, 0
    for num in array:
        res ^= num
    # 从右向左找到第一个为1的位
    tmp = 0
    for i in range(32):
        if (res >> i) & 1 == 1:
            tmp = i
            break
    # 将第 tmp 位为1的数据划分成一组
    for num in array:
        if (num >> tmp) & 1 == 1:
            x ^= num
        else:
            y ^= num

    return x, y
```

🍥 **考察要点**：数组、位运算、哈希
🍬 **解题思路**：**哈希**法的空间复杂度为 O(n)；**位运算**中异或运算：`n^0 = n`, `n^n = 0`, `n^n^m = n^(n^m)`.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
