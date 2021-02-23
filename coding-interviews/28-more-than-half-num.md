# 28 数组中出现次数超过一半的数字

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

## 题解

```python
def more_than_half_num(numbers):
    """ 哈希法 """
    length = len(numbers)
    tmp = {}
    for i in range(length):
        num = numbers[i]
        if tmp.get(num, 0) > length // 2:
            return num
        if num not in tmp:
            tmp[num] = 1
        else:
            tmp[num] += 1
    return 0
```

```python
def more_than_half_num(numbers):
    """ 排序法 """
    numbers.sort()
    cond = numbers[len(numbers) // 2]
    if numbers.count(cond) > len(numbers) // 2:
        return cond
    return 0
```

```python
def more_than_half_num(numbers):
    """ 候选法 """
    if not numbers:
        return 0
    res = numbers[0]
    times = 1
    length = len(numbers)
    for i in range(1, length):
        if times == 0:
            res = numbers[i]
            times = 1
        elif res == numbers[i]:
            times += 1
        else:
            times -= 1

    return res if numbers.count(res) * 2 > length else 0
```

🍥 **考察要点**：数组、排序、哈希、候选

🍬 **解题思路**：

- **哈希法**：创建一个哈希表存储数组中每个元素出现的次数。时间/空间复杂度均为 *O(n)*;
- **排序法**：对数组排序，再判断数组中间的值是否为众数。时间复杂度为 *O(nlogn)*, 空间复杂度为 *O(1)*;
- **候选法**：分叶法，对数组同时去掉两个不同的数字，到最后剩下的数字就是所求的数字。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
