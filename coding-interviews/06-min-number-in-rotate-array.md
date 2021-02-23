# 06 旋转数组的最小数字

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。例如数组[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

## 题解

```python
def min_number_in_rotate_array(rotate_array):
    if len(rotate_array) == 0:
        return 0

    first, last = 0, len(rotate_array) - 1
    while first < last:
        if rotate_array[first] < rotate_array[last]:
            return rotate_array[first]

        mid = first + ((last - first) >> 1)
        if rotate_array[mid] > rotate_array[last]:
            first = mid + 1
        elif rotate_array[mid] < rotate_array[last]:
            last = mid
        else:
            last -= 1

    return rotate_array[first]
```

🍥 **考察要点**：数组、二分查找

🍬 **解题思路**：二分查找的变种。

- target 选**右端点**，arr[mid] 与 target 比较。

- 若 `arr[mid] > target` , 确定区间为 `[mid+1, last]` ; 若 `arr[mid] < target`  , 确定区间为 `[first, mid]` . 若相等，`last--` .

*二分查找的一般比较原则*：

- 有目标值，直接让 arr[mid] 和 target 比较；
- 没有目标值，一般考虑**端点**。

🍉 **时间复杂度**：O(logn)

🍭 **空间复杂度**：O(1)

🍣 **延伸**：若换成非递增排序数组呢？

- target 选**左端点**；
- 若 `arr[mid] > target` , 确定区间为 `[first, mid]` ;
- 若 `arr[mid] < target` , 确定区间为 `[mid+1, last]` ;
- 若相等，`first++` .
