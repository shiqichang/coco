# 44 翻转单词顺序列

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

## 题解

```python
def reverse_sentence(s):
    """ 分割➕倒序 """
    return " ".join(s.split(" ")[::-1])
```

```python
def reverse_sentence(s):
    """ 双指针法 """
    ss = s.strip()
    if not ss:
        return s
    i = j = len(ss) - 1
    res = []
    while i >= 0:
        while i >= 0 and ss[i] != ' ':  # 搜索首个空格
            i -= 1
        res.append(ss[i+1:j+1])  # 添加单词
        while ss[i] == ' ':  # 跳过单词间空格
            i -= 1
        j = i  # j 指向下一个单词的尾字符
    return ' '.join(res)
```

🍥 **考察要点**：字符串
🍬 **解题思路**：分割➕倒序；双指针法。

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
