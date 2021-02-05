# 02 序列构成的数组

## 内置序列类型

- 容器序列
  - `list, tuple, collections.deque` 能存放不同类型的数据；
  - 存放的是所包含的任意类型的对象的 `引用`；
- 扁平序列
  - `str, bytes, bytearray, memoryview, array.array` 只能容纳一种类型；
  - 存放的是 `值`，而不是引用；
  - 其实是一段连续的内存空间。

按照能否被修改来分类：

- 可变序列 (MutableSequence)
  - `list, bytearray, array.array, collections.deque, memoryview`
- 不可变序列 (Sequence)
  - `tuple, str, bytes`

## 具名元组

`collections.namedtuple` 是一个工厂函数，用来构建一个带字段名的元组和一个有名字的类。

- `_fields` 属性是一个包含这个类所有字段名称的元组；
- 用 `_make()` 通过接受一个可迭代对象来生成这个类的一个实例；
- `_asdict()` 把具名元组以 `collections.OrderedDict` 的形式返回。
