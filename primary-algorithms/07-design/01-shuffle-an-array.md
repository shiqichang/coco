# 01 打乱数组

> 🌈 **初级算法系列之设计模式**
>
> 你的无畏源于无知。

## 题目描述

打乱一个没有重复元素的数组。

### 示例

> // 以数字集合 1, 2 和 3 初始化数组。
> int[] nums = {1,2,3};
> Solution solution = new Solution(nums);
>
> // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
> solution.shuffle();
>
> // 重设数组到它的初始状态[1,2,3]。
> solution.reset();
>
> // 随机返回数组[1,2,3]打乱后的结果。
> solution.shuffle();

## 题解

```python
class Solution(object):
    """ 暴力法 """
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)
        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)
        return self.array
```

```python
class Solution(object):
    """ Fisher-Yates 洗牌算法 """
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
```

🍥 **考察要点**：Fisher-Yates 洗牌算法

🍬 **解题思路**：暴力法，时间复杂度为 O(n^2)；**Fisher-Yates 洗牌算法**。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(n)
