# 51 构建乘积数组

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素`B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]`。不能使用除法。（注意：规定`B[0]=A[1]*A[2]*...*A[n-1]`，`B[n-1]=A[0]*A[1]*...*A[n-2]`;）对于A长度为1的情况，B无意义，故而无法构建，该情况不会存在。

## 题解

```python
def multiply(A):
    """ 双重循环 """
    B = []
    length = len(A)
    if length == 0:
        return B
    for i in range(length):
        tmp = A[i]
        A[i] = 1
        Bi = 1
        for j in A:
            Bi *= j
        B.append(Bi)
        A[i] = tmp
    return B
```

```python
def multiply(A):
    """ 上三角 * 下三角 """
    length = len(A)
    if length == 0:
        return []
    B, tmp = [1] * length, 1
    for i in range(1, length):
        B[i] = B[i-1] * A[i-1]  # 下三角
    for i in range(length-2, -1, -1):
        tmp *= A[i+1]  # 上三角
        B[i] *= tmp  # 下三角 * 上三角
    return B
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gitgyb0whbj30pq0ieq5y.jpg)

🍥 **考察要点**：数组

🍬 **解题思路**：双重循环，`A[i]` 赋值为 1，时间复杂度为 O(n^2); 把 `B[i]` 看成 `A[0]A[1]...A[i-1]`和`A[i+1]...A[n-2]A[n-1]`两部分的乘积。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
