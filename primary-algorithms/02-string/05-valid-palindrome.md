# 05 验证回文串

> 🌈 **初级算法系列之数组**
>
> 你的无畏源于无知。

## 题目描述

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
**说明：** 本题中，我们将空字符串定义为有效的回文串。

### 示例1

> 输入: "A man, a plan, a canal: Panama"
> 输出: true

### 示例2

> 输入: "race a car"
> 输出: false

## 题解

```python
# 筛选➕判断
def is_palindrome(s):
    """ 字符串翻转API """
    sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
    return sgood == sgood[::-1]
```

```python
# 筛选➕判断
def is_palindrome(s):
    """ 双指针法 """
    sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
    n = len(sgood)
    left, right = 0, n - 1
    while left < right:
        if sgood[left] != sgood[right]:
            return False
        left, right = left + 1, right - 1
    return True
```

```python
def is_palindrome(s):
    """ 在原字符串上直接判断：双指针法 """
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
            
    return True
```

🍥 **考察要点**：双指针
🍬 **解题思路**：筛选➕判断，字符串翻转或双指针法，空间复杂度为 O(n)；在原字符串上直接判断

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(1)
