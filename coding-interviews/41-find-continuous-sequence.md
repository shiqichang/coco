# 41 和为S的连续正数序列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

### 输入描述

> 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

## 题解

```python
def find_continuous_sequence(target):
    """ 滑动窗口 """
    i = 1  # 滑动窗口的左边界
    j = 1  # 滑动窗口的右边界
    tsum = 0  # 滑动窗口中数字的和
    res = []

    while i <= target // 2:
        if tsum < target:
            # 右边界向右移动
            tsum += j
            j += 1
        elif tsum > target:
            tsum -= i
            i += 1
        else:
            # 记录结束
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            tsum -= i
            i += 1
    return res
```

```python
def find_continuous_sequence(target):
    """ 求根法 """
    res = []
    if target == 1:
      return res

    # y 不能超过 target 的中值，即 y<=target//2 + 1
    for y in range(1, target // 2 + 2):
        x = (1/4 + y**2 + y - 2*target) ** (1/2) + 1/2
        if type(x) != complex and x - int(x) == 0:
            res.append(list(range(int(x), y+1)))

    return res
```

```python
def find_continuous_sequence(target):
    """ 间隔法 """
    i, res = 1, []
    while i*(i+1)/2 < target:
        if not (target - i*(i+1)/2) % (i+1):
            x = int(target - i*(i+1)/2) // (i+1)
            res.append(list(range(x, x+i+1)))
        i += 1
    # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入res的
    return res[::-1]
```

🍥 **考察要点**：数学、前缀和、滑动窗口、求根法
🍬 **解题思路**：

- **滑动窗口**：一个左闭右开区间 `[i, j)`. 其性质是*窗口的左边界和右边界永远只能向右移动。*
- **求根法**：等差数列公式为 `Sn = n(a1+an) / 2`.
  - 由 `(x+y)(y-x+1) / 2 = t` 可得 `x^2-x-y^2-y+2t = 0`;
  - 由求根公式 `x1,2 = (-b +- (b^2-4ac)^(1/2)) / 2a` 可得 `x = (y^2+y-2t+1/4)^(1/2) + 1/2`.
- **间隔法**：`i = y - x`
  - 由 `(2x+i)(i+1)/2 = t` 可得 `x = (t - i(i+1)/2) / (i+1)`l
  - 由于 `x` 必须是正整数，故 `i(i+1)/2` 必须小于 `t`.

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
