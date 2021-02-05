# 04 杨辉三角

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

### 示例

> 输入: 5
> 输出:
>
> ```shell
> [
>      [1],
>     [1,1],
>    [1,2,1],
>   [1,3,3,1],
>  [1,4,6,4,1]
> ]
> ```

## 题解

```python
def generate(num_rows):
    triangle = []
    for row_num in range(num_rows):
        # The first and last low elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            
        triangle.append(row)
        
    return triangle
```

🍥 **考察要点**：动态规划
🍬 **解题思路**：动态规划。

🍉 **时间复杂度**：O(n^2)
🍭 **空间复杂度**：O(n^2)
