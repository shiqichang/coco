# 02 汉明距离

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

两个整数之间的[汉明距离](https://baike.baidu.com/item/汉明距离)指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 `x` 和 `y`，计算它们之间的汉明距离。
**注意：** 0 ≤ `x`, `y` < 231.

### 示例

> 输入: x = 1, y = 4
>
> 输出: 2
>
> 解释:
> 1   (0 0 0 1)
> 4   (0 1 0 0)
> ↑   ↑
>
> 上面的箭头指出了对应二进制位不同的位置。
>

## 题解

```python
def hamming_distance(x, y):
    """ 内置位计数功能 """
    return bin(x ^ y).count('1')
```

```python
def hamming_distance(x, y):
    """ 移位 """
    xor = x ^ y
    distance = 0
    while xor:
        # mask out the rest bits
        if xor & 1:
            distance += 1
        xor >>= 1  # 右移
    return distance
```

```python
def hamming_distance(x, y):
    """ 布赖恩-克尼恩算法 """
    xor = x ^ y
    distance = 0
    while xor:
        distance += 1
        # remove the rightmost bit of '1'
        xor = xor & (xor - 1)
    return distance
```

🍥 **考察要点**：XOR 位运算(当且仅当输入位不同时输出为1)
🍬 **解题思路**：内置位计数功能；**移位**，进行逻辑移位，移入零替换丢弃的位，使用取模运算 `i % 2` 或 AND 操作 `i & 1`,屏蔽最右位以外的其他位；**布赖恩-克尼恩算法**，使用特定比特位和算术运算移除等于1的最右比特位。

🍉 **时间复杂度**：O(1)
🍭 **空间复杂度**：O(1)
