# 05 将有序数组转换为二叉搜索树

> 🌈 **初级算法系列之树**
>
> 你的无畏源于无知。

## 题目描述

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1。

### 示例

> 给定有序数组: [-10,-3,0,5,9],
>
> 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
>
> ```shell
>       0
>      / \
>    -3   9
>    /   /
>  -10  5
> ```

## 题解

```python
def sorted_array_to_bst(nums):
    def helper(left, right):
        if left > right:
            return None
        
        # 总是选择中间位置左边的数字作为根结点
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(nums) - 1)
```

![1](https://tva1.sinaimg.cn/large/007S8ZIlly1gj1lencajsj30mc0ekgng.jpg)

```python
def sorted_array_to_bst(nums):
    def helper(left, right):
        if left > right:
            return None

        # 总是选择中间位置右边的数字作为根结点
        mid = (left + right + 1) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(nums) - 1)
```

![2](https://tva1.sinaimg.cn/large/007S8ZIlly1gj1lf7snebj30mo0ei766.jpg)

```python
def sorted_array_to_bst(nums):
    def helper(left, right):
        if left > right:
            return None

        # 选择任意一个中间位置数字作为根结点
        mid = (left + right + random.randint(0, 1)) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(nums) - 1)
```

![3](https://tva1.sinaimg.cn/large/007S8ZIlly1gj1lgejxkoj30xa0eotca.jpg)

🍥 **考察要点**：中序遍历

🍬 **解题思路**：**中序遍历**，二叉搜索树的中序遍历是升序遍历。

1. *总是选择中间位置左边的数字作为根结点*
2. *总是选择中间位置右边的数字作为根结点*
3. *选择任意一个中间位置数字作为根结点*

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(logn)
