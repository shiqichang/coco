# 01 Fizz Buzz

> 🌈 **初级算法系列之数学**
>
> 你的无畏源于无知。

## 题目描述

写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3. 如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

### 示例

> n = 15,
>
> 返回:
> [
> "1",
> "2",
> "Fizz",
> "4",
> "Buzz",
> "Fizz",
> "7",
> "8",
> "Fizz",
> "Buzz",
> "11",
> "Fizz",
> "13",
> "14",
> "FizzBuzz"
> ]

## 题解

```python
def fizz_buzz(n):
    """ 字符串连接 """
    res = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if not s:
            s = str(i)
        res.append(s)
    return res
```

```python
def fizz_buzz(n):
    """ 散列表 """
    ans = []
    fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
    for num in range(1, n+1):
        num_ans_str = ""
        for key in fizz_buzz_dict.keys():
            if num % key == 0:
                num_ans_str += fizz_buzz_dict[key]
        if not num_ans_str:
            num_ans_str = str(num)
        ans.append(num_ans_str)
    return ans
```

🍥 **考察要点**：散列表

🍬 **解题思路**：模拟法；字符串连接；散列表。

🍉 **时间复杂度**：O(n)

🍭 **空间复杂度**：O(1)
