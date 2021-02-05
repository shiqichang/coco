# 65 矩阵中的路径

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

## 题解

```python
# board 为二维数组
def has_path(board, word):
    def dfs(i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp, board[i][j] = board[i][j], '/'
        res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
        board[i][j] = tmp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
```

```python
# matrix 为字符串
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.findPath(i, j, path[1:], list(matrix), rows, cols):
                        return True
        return False
        
    def findPath(self, i, j, path, matrix, rows, cols):
        if i < 0 or j < 0 or i > rows or j > cols:
            return False
        if not path:
            return True
        matrix[i*cols+j] = None
        if i+1 < rows and matrix[(i+1)*cols+j] == path[0]:
            if self.findPath(i+1, j, path[1:], matrix, rows, cols):
                return True
        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            if self.findPath(i, j+1, path[1:], matrix, rows, cols):
                return True
        if i-1>=0 and matrix[(i-1)*cols+j] == path[0]:
            if self.findPath(i-1, j, path[1:], matrix, rows, cols):
                return True
        if j-1>=0 and matrix[i*cols+j-1] == path[0]:
            if self.findPath(i, j-1, path[1:], matrix, rows, cols):
                return True
        else:
            return False
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1giuxnsmo4aj314i0n0ae2.jpg)

🍥 **考察要点**：深度优先搜索 DFS、回溯
🍬 **解题思路**：深度优先搜索➕剪枝。

🍉 **时间复杂度**：O(3^k*mn)
🍭 **空间复杂度**：O(k)
