# 07 函数装饰器和闭包

## 使用 functools.lru_cache 做备忘

- `functools.lru_cache` 是很实用的装饰器，实现了备忘（memoization）功能。把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。
- `LRU, Least Recently Used`, 表明缓存不会无限制增长，一段时间不用的缓存条目会被扔掉。
