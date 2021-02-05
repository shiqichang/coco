# 04 重建二叉树

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

## 题解

```java
import java.util.Arrays;

public class Solution {

    public static TreeNode reConstructBinaryTree(int[] pre,int[] in) {
        if (pre.length == 0 || in.length == 0) {
            return null;
        }
        TreeNode root = new TreeNode(pre[0]);
        for (int i=0; i<in.length; i++) {
            if (in[i] == pre[0]) {
                root.left = reConstructBinaryTree(Arrays.copyOfRange(pre, 1, i+1), Arrays.copyOfRange(in, 0, i));
                root.right = reConstructBinaryTree(Arrays.copyOfRange(pre, i+1, pre.length), Arrays.copyOfRange(in, i+1, in.length));
                break;
            }
        }
        return root;
    }
}
```

```python
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return
        root = TreeNode(pre[0])
        for i in range(len(tin)):
            if tin[i] == pre[0]:
                root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
                root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
                break
        return root
```

🍥 **考察要点**：树、递归
🍬 **解题思路**：前序遍历数组的首元素是根节点，根据根节点的值在中序遍历数组中找到根节点的位置，根节点左边的是左子树，右边的是右子树。

*前序遍历是根左右，中序遍历是左根右，后序遍历是左右根。*

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)

在官方解法 C++ 实现中，对 `pre_left + root_index - vin_left` 的解释：

- `root_index - vin_left` 为根节点左边有几个元素；
- `pre_left + root_index - vin_left` 为从 `pre_left` 开始往后推这么多元素。
