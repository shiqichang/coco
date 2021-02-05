# 45 扑克牌顺子

> 🌟 **剑指 Offer 系列**
>
> 给岁月以文明，而不是给文明以岁月。

## 题目描述

LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

## 题解

```python
def is_continuous(numbers):
    """ 集合 Set➕遍历 """
    if not numbers:
        return False
    
    repeat = set()
    ma, mi = 0, 14
    for num in numbers:
        if num == 0:  # 跳过大小王
            continue
        ma = max(ma, num)  # 最大牌
        mi = min(mi, num)  # 最小牌
        if num in repeat:
            return False  # 若有重复，提前返回 false
        repeat.add(num)
    return ma - mi < 5  # 最大牌-最小牌 < 5，则可构成顺子
```

```python
def is_continuous(numbers):
    """ 排序➕遍历 """
    if not numbers:
        return False
    joker = 0
    numbers.sort()
    for i in range(4):
        if numbers[i] == 0:
            joker += 1  # 统计大小王数量
        elif numbers[i] == numbers[i+1]:
            return False  # 若有重复，提前返回 false
    return numbers[4] - numbers[joker] < 5
```

🍥 **考察要点**：数组、set、排序
🍬 **解题思路**：5张牌是顺子的充分条件是*除大小王外，所有牌无重复；`max-min < 5`*. 集合➕遍历；排序➕遍历，其时间复杂度为 O(nlogn), 空间复杂度为 O(1).

🍉 **时间复杂度**：O(n)
🍭 **空间复杂度**：O(n)
