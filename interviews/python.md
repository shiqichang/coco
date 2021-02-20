# Python

## 1 Python 的函数参数传递

- 变量可以理解是内存中一个对象的“引用”；
- 类型是属于对象的，而不是变量；
- 可更改(mutable)对象：字典、列表、集合
- 不可更改(immutable)对象：数字、字符串、元组
- Python 函数传参是传对象引用。如果传的是可变对象的引用，相当于“传引用”来传递对象，如果传的是不可变对象的引用，相当于“传值”来传递对象。

## 2 Python 中的元类

- 类是一组用来描述如何生成一个对象的代码段。在 Python 中类也是对象，可以在运行时动态创建它们。

### type

type 能动态的创建类。type(类名, 父类的元组, 包含属性的字典)
type 就是一个元类，type 是 Python 中创建所有类的元类。type 是它自己的元类。
str 创建字符串对象，int 创建整数对象，type 创建类对象。可以通过检查 `__class__` 属性来看到这一点。

Python 中所有东西都是对象，包括整数、字符串、类、函数等。

元类的目的是创建类时能够自动地更改类。
通常会使用元类去做一些晦涩的事情，依赖于自省，控制继承等。

```python
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    uppercase_attr = {}

    for name, val in future_class_attr.items():
        if not name.startswith("__"):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr
```

```python
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}

        for name, val in dct.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
```

### `__slots__`

Python 允许在定义 class 时，定义一个特殊的 `__slots__` 变量，来限制该 class 实例能添加的属性。`__slots__` 定义的属性仅对当前类实例起作用，对继承的子类不起作用。

如果定义了 `__slots__` , 还想在之后添加新的变量，就把 `__dict__` 添加到 `__slots__` 元组中；还会消失的一个属性是 `__weakref__` , 若还想支持实例的 weak reference, 可以把 `__weakref__` 添加到 `__slots__` 元组中。

`__slots__` 是通过 descriptor 实现的，会为每个变量创建一个 descriptor.

元类的主要用途是创建 API.
如 `Django ORM models.Model` 定义了 `__metaclass__`, 并使用一些魔法将定义的简单类转变成对数据库的一个复杂 hook.

## 3 @staticmethod 和 @classmethod

```shell
\          实例方法     类方法             静态方法
a = A()    a.foo(x)    a.class_foo(x)    a.static_foo(x)
A          不可用       A.class_foo(x)    A.static_foo(x)
```

## 4 类变量和实例变量

- 类变量：可在类的所有实例之间共享的值。
- 实例变量：实例化后，每个实例单独拥有的变量。

```python
class Person(object):
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name, p2.name, Person.name)
# bbb aaa aaa
```

`p1.name` 是实例调用了类变量，其实是函数传参的问题。`p1.name` 一开始指向的类变量 `name`，但在实例的作用域里把类变量的引用改变了，就变成了一个实例变量，`self.name` 不再引用 `Person` 的类变量 `name`.

## 5 Python 自省

**自省：** 在运行时能够获取对象的类型。

Python 常见的自省(introspection)机制(函数用法)有：`dir(), type(), hasattr(), getattr(), isinstance()`

## 6 字典推导式

```python
import random

random_dict = {i: random.randint(10, 100) for i in range(1, 5)}
print(random_dict)
# {1: 37, 2: 68, 3: 75, 4: 83}
```

<!-- here -->
<!-- here -->
<!-- here -->

## 7 Python 中单下划线和双下划线

- `__foo__`: 一种约定，python 内部的名字，用来区分其他用户自定义的命名；
- `_foo`: 一种约定，protected, 用来指定变量私有，不能用 from module import * 导入，其他的和公有一样访问；
- `__foo`: private, 解释器用 _classname__foo 来代替，以区别和其他类相同的命名。

```python
class MyClass(object):

    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", word"


mc = MyClass()
print(mc.__dict__)
# {'_MyClass__superprivate': 'Hello', '_semiprivate': ', word'}
print(mc._MyClass__superprivate)
# Hello
```

## 8 字符串格式化：% 和 .format

```python
import datetime

name = ('1', '2', '3')
print("hi there is %r" % (name, ))
print("hi there is {!r}".format(name))
# hi there is ('1', '2', '3')

points = 19
total = 22
print("Correct answers: {:.2%}".format(points / total))
# Correct answers: 86.36%

d = datetime.datetime.now()
print("{:%Y-%m-%d %H:%M:%S}".format(d))
# 2021-01-14 20:11:52

print("{:,}".format(1234567890))
# 1,234,567,890

print("repr() show quotes: {!r}, str() doesn't: {!s}".format("test1", "test2"))
# repr() show quotes: 'test1', str() doesn't: test2

name = "jack"
age = 18
sex = "man"
job = "IT"
salary = 9999.99
print(f"My name is {name.capitalize()}.")
# My name is Jack.
print(f"I am {age:*^10} years old.")
# I am ****18**** years old.
print(f"I am a {sex}.")
# I am a man.
print(f"My salary is {salary:10.3f}")
# My salary is   9999.990
```

## 9 迭代器和生成器

Python 中关键字 yield

- iterables(可迭代对象)：`__iter__()` 返回一个特殊的迭代器对象, 可以用在 for…in… 语句中的都是可迭代的；
- iterators(迭代器)：`__next__()` 会返回下一个迭代器对象;
- generators(生成器)：迭代器的一种，只能迭代它一次。它和迭代器的区别是用 () 代替了 [].

`list.extend()`: 只希望接受一个迭代器，不管是 strings, lists, tuples 或 generators. 这种方法叫 duck typing.

```python
import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)  # 排列
print(races)
# <itertools.permutations object at 0x7fb015445678>
```

## 10 *args 和 **kwargs

*args 为 位置参数，**kwargs 为关键字参数，在这两种参数前面的叫命名参数。

`*` 的作用有两个，打包参数(pack)和拆分(或解包)参数(unpack).

```python
def print_everything(*args):  # pack
    for count, thing in enumerate(args):
        print("{0}. {1}".format(count, thing))


print_everything("apple", "orange", "banana")
print_everything(*["apple", "orange", "banana"])  # unpack


def table_things(**kwargs):
    for name, value in kwargs.items():
        print("{0} = {1}".format(name, value))


table_things(apple="fruit", cabbage="vegetable")
```

## 11 面向切面编程 AOP 和装饰器

装饰器：一种设计模式，被用于有切面需求的场景，如插入日志、性能测试、事务处理等。作用是为已存在的对象添加额外的功能。

```python
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)


sandwich()
# </''''''\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>
```

### 高级用法

#### 1) 在装饰器函数里传入参数

```python
def a_decorator_passing_args(function_to_decorate):
    def a_wrapper_accepting_args(arg1, arg2):
        print("I got args! Look:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_args


@a_decorator_passing_args
def print_full_name(first_name, last_name):
    print("My name is", first_name, last_name)


print_full_name("Peter", "Venkman")
# I got args! Look: Peter Venkman
# My name is Peter Venkman
```

#### 2) 装饰方法

```python
def method_friendly_decorator(method_to_decorate):
    print(method_to_decorate, 111)

    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        self, lie = args
        lie -= 3
        args = self, lie
        return method_to_decorate(*args, **kwargs)
    print(wrapper, 333)
    return wrapper


class Lucy(object):

    def __init__(self):
        print(self, 555)
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print(self, 444)
        s = "I am %s, what did you think?" % (self.age + lie)
        return s


l = Lucy()
print(l.say_your_age)
print(l.say_your_age(-3))
# <function Lucy.say_your_age at 0x7fe74627c158> 111
# <function method_friendly_decorator.<locals>.wrapper at 0x7fe74627c1e0> 333
# <__main__.Lucy object at 0x7fe741f5ca90> 555
# <bound method method_friendly_decorator.<locals>.wrapper of <__main__.Lucy object at 0x7fe741f5ca90>>
# (<__main__.Lucy object at 0x7fe741f5ca90>, -3)
# {}
# <__main__.Lucy object at 0x7fe741f5ca90> 444
# I am 26, what did you think?
```

#### 3) 把参数传递给装饰器

##### 装饰器只能被调用一次

```python
def decorator_maker_with_args(decorator_arg1, decorator_arg2):
    print("I make decorators! args:", decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("I am the decorator. args:", decorator_arg1, decorator_arg2)

        def wrapped(function_arg1, function_arg2):
            print("I am the wrapper around the decorated function. args:",
                  decorator_arg1, decorator_arg2, function_arg1, function_arg2)
            return func(function_arg1, function_arg2)
        return wrapped
    return my_decorator


@decorator_maker_with_args("Leonard", "Sheldon")
def decorated_function_with_args(function_arg1, function_arg2):
    print("I am the decorated function. args:", function_arg1, function_arg2)


decorated_function_with_args("Rajesh", "Howard")
# I make decorators! args: Leonard Sheldon
# I am the decorator. args: Leonard Sheldon
# I am the wrapper around the decorated function. args: Leonard Sheldon Rajesh Howard
# I am the decorated function. args: Rajesh Howard
```

##### 装饰装饰器

```python
def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Decorated with", *args, **kwargs)
        return func(function_arg1, function_arg2)
    return wrapper


@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print("Hello", function_arg1, function_arg2)


decorated_function("Universe and", "everything")
# Decorated with 42 404 1024
# Hello Universe and everything
```

##### `functools.wraps()` 函数可以复制装饰器函数的名字，模块及文档给它的包装器

```python
import functools


def bar(func):

    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper


@bar
def foo():
    print("foo")


print(foo.__name__)  # foo
```

Python 自身提供了几个装饰器，如 `property, staticmethod`.
Django 用装饰器来管理缓存和视图的权限；Twisted 用来修改异步函数的调用。

## 12 鸭子类型

我们不关心对象是什么类型，到底是不是鸭子，只关心行为。

- 比如 Python 中，有很多 file-like 的东西，如 StringIO, GzipFile, socket, 它们有很多相同的方法，我们把它们当作文件使用。
- 又比如 list.extend() 方法，我们不关心它的参数是不是 list, 只要它是可迭代的，所有它的参数可以是 list/tuple/dict/字符串/生成器等。

## 13 Python 中重载

函数重载是解决两个问题：1 可变参数类型；2 可变参数个数。
**一个基本的设计原则**：仅仅当两个函数除了参数类型和参数个数不同以外，其功能完全相同，此时才使用函数重载。

- 对于情况1，Python 可以接受任何类型的参数；
- 对于情况2，Python 通过缺省参数处理。故 Python 不需要函数重载。

## 14 新式类和旧式类

新式类早在 2.2 就出现了，所以旧式类完全是兼容的问题。Python 3 只有新式类。
**MRO(Method Resolution Order, 方法解析顺序) 问题**：新式类继承是根据 C3 算法，广度优先，旧式类是深度优先。

```python
class A:

    def __init__(self):
        pass

    def save(self):
        print("This is from A")


class B(A):

    def __init__(self):
        pass


class C(A):

    def __init__(self):
        pass

    def save(self):
        print("This is from C")


class D(B, C):

    def __init__(self):
        pass


fun = D()
fun.save()
# 旧式类：This is from A
# 新式类：This is from C


class B(object):  # 新式类
    pass


class C:  # 旧式类
    pass


print(dir(B))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(dir(C))
# ['__doc__', '__module__']
```

- `__repr__` 的目的是对象信息唯一性，`__str__` 的目的是对象信息可读性。
- 新式类增加了 `__class__`, `__slots__`, `__getattribute__` 属性。

## 15 `__new__` 和 `__init__` 的区别

- `__new__` 是一个静态方法，`__init__` 是一个实例方法；
- `__new__` 方法会返回一个创建的实例，`__init__` 什么都不返回；
- 只有在 `__new__` 返回一个 cls 的实例时后面的 `__init__` 才会被调用；
- 当创建一个新实例时调用 `__new__`, 初始化一个实例时调用 `__init__`.

ps: `__metaclass__` 是创建类时起作用；故我们可以分别使用 `__metaclass__`, `__new__`, `__init__` 来分别在类创建、实例创建、实例初始化时做些手脚。

`__new__` 为什么是静态方法，而不是类方法？

1. cls 只是一个变量名，并不代表什么；
2. 要创建一个类，必须需要当前类的信息
3. 第一个参数可以不是当前类（而是其他类，比如 base 类），当有继承结构时，需要在 base 类里调用 `__new__` 来创建子类的对象；
4. 在 factory design pattern 里常用的。

## 16 单例模式

一个类只有一个实例，且该实例易于外界访问，从而方便对实例个数的控制及节约系统资源。

### 1) 使用 `__new__` 方法

```python
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance


class MyClass(Singleton):

    def __init__(self, x):
        self.x = x


print(id(MyClass(10)))
print(id(MyClass(20)))
# 140353522382384
```

### 2) 共享属性

创建实例时把所有实例的 `__dict__` 指向同一个字典，这样它们具有相同的属性和方法。

```python
class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):

    def __init__(self, x):
        self.x = x


print(id(MyClass2(10)))
print(id(MyClass2(20)))
# 140730566194848
```

### 3) 装饰器版本

```python
def singleton(cls):
    instance = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    
    return get_instance
```

```python
import functools


def singleton(cls):
    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it

        cls.__it__ = it = cls.__new_original__(cls, *args, **kwargs)
        it.__init_original__(*args, **kwargs)
        return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__

    return cls


@singleton
class Foo(object):

    def __new__(cls, *args, **kwargs):
        cls.x = 10
        return object.__new__(cls)

    def __init__(self):
        assert self.x == 10
        self.x = 15


assert Foo().x == 15
Foo().x = 20
assert Foo().x == 20
print(Foo.__it__)
print(Foo.__it__)
# <__main__.Foo object at 0x7ffba7d803c8>
# <__main__.Foo object at 0x7ffba7d803c8>
```

### 4) import 方法

```python
# my_singleton.py
class MySingleton(object):
    
    def foo(self):
        pass
    

my_singleton = MySingleton()

# to use
from my_singleton import my_singleton

my_singleton.foo()
```

**保证两点**：1 从多线程下是否可以保证单实例；2 单实例化时是否可以传入初始参数。

情况 1 可以使用同步锁解决多线程的冲突。
如果项目中不需要使用线程相关机制，则没必要，因为多线程环境会启动 GIL 锁相关的逻辑，这会影响 Python 程序运行速度。

```python
def synchronous_lock(func):
    def wrapper(*args, **kwargs):
        with threading.Lock():
            return func(*args, **kwargs)
    return wrapper
```

## 17 Python 中的作用域

**作用域**：一个 Python 程序可以直接访问命名空间的正文区域。
当 Python 中遇到一个变量时会按照这样的顺序进行搜索：

- 本地作用域(Local) -> 当前作用域被嵌入的本地作用域(Enclosing Local) -> 全局/模块作用域(Global) -> 内置作用域(Built-in)

**命名空间**：从名称到对象的映射，大部分都是通过 Python 字典实现。生命周期取决于对象的作用域。

- 局部命名空间(local namespace) -> 全局命名空间(global namespace) -> 内置命名空间(built-in namespace)

### global 和 nonlocal 关键字

```python
num = 1


def fun1():
    global num  # global 关键字声明
    print(num)  # 1
    num = 123
    print(num)  # 123


fun1()
print(num)  # 123


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal 关键字声明
        num = 100
        print(num)  # 100

    inner()
    print(num)  # 100


outer()
```

## 18 GIL 线程全局锁

**全局解释器锁(Global Interpreter Lock)**: Python 为了保证线程安全而采取的独立线程运行的限制。
对于 io 密集型任务，Python 的多线程起到作用，但对于 cpu 密集型任务，Python 的多线程几乎占不到任何优势，还有可能因为争抢资源而变慢。
解决办法是多进程和协程(单 cpu, 能减少切换代价提升性能)。

## 19 闭包

**闭包(closure)** 是函数式编程的重要语法结构。当一个内嵌函数引入其外部作用域的变量，就会得到一个闭包。
**闭包**：可以由另一个函数动态生成的函数，并且可以改变和存储函数外创建的变量的值。

创建一个闭包必须满足：

- 必须有一个内嵌函数
- 内嵌函数必须引用外部函数中的变量
- 外部函数的返回值必须是内嵌函数

```python
def fun1():
    a = 1

    def fun2():  # 嵌套函数
        nonlocal a
        a += 1
        print("fun2 -- a = ", a)  # fun2 -- a =  2

    fun2()
    print("fun1 -- a = ", a)  # fun1 -- a =  2


fun1()


# 二元一次方程
def fun(a, b, c):
    def para(x):  # 闭包
        return a*x**2 + b*x + c
    return para


f = fun(1, 2, 3)
print(f(2))  # 11
```

### Python 循环中不包括域的概念

```python
flist = []

for i in range(3):
    def make_func(i):
        # 在 func 外面再定义一个 makefunc 函数，func 形成闭包
        def func(x):
            return x * i
        return func
    flist.append(make_func(i))


for f in flist:
    print(f(2))  # 0 2 4
```

## 20 lambda 函数

lambda(匿名函数) 与 def 的区别：

- lambda 会返回一个函数对象，但它不会赋给一个标识符，def 会把函数对象赋值给一个变量；
- lambda 是一个表达式，def 是一个语句；
- 像 if, for, print 等语句不能用于 lambda.

```python
l = lambda: None
print(l(), l, l.__class__)
# None <function <lambda> at 0x7fc516d8a840> <class 'function'>

l1 = lambda *args: sum(args)
print(l1(1, 2))  # 3

l2 = lambda **kwargs: 1
print(l2(name="cc"))  # 1

g = [lambda a: a*2, lambda b: b*3]
print(g[0](5))  # 10
print(g[1](6))  # 18
```

用法扩展：

1. 赋值给一个变量，通过该变量间接调用；e.x add = lambda x, y: x + y
2. 赋值给其他函数；e.x time.sleep = lambda x: None
3. 作为参数传递给其他函数；e.x return lambda x, y: x + y，嵌套函数

部分 Python 内置函数接受函数作为参数，有 filter(), sorted(), map(), reduce().

```python
import functools

f1 = filter(lambda x: x % 3 == 0, [1, 2, 3])
print(f1, list(f1))  # <filter object at 0x7ff8765825c0> [3]

s1 = sorted([1, 2, 3, 4, 5, 6, 7, 8], key=lambda x: abs(5 - x))
print(s1)  # [5, 4, 6, 3, 7, 2, 8, 1]

m1 = map(lambda x: x + 1, [1, 2, 3])
print(m1, list(m1))  # <map object at 0x7ff876582320> [2, 3, 4]

r1 = functools.reduce(lambda a, b: "{}, {}".format(a, b), [1, 2, 3, 4, 5, 6])
print(r1)  # 1, 2, 3, 4, 5, 6
```

## 21 Python 函数式编程

三大特性：

- immutable data 不可变数据
- first class functions
- 尾递归优化

几个技术：

- map & reduce
- pipeline
- recursing 递归
- curring
- higher order function 高阶函数

一些好处：

- parallelization 并行
- lazy evaluation 惰性求值
- determinism 确定性

准则：不依赖于外部的数据，且不改变外部数据的值，而是返回一个新的值

```python
import functools

num = [2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]
positive_num = list(filter(lambda x: x > 0, num))
average = functools.reduce(lambda x, y: x + y, positive_num) / len(positive_num)
print(average)  # 5.0
```

## 22 Python 里的拷贝

引用和 copy(), deepcopy() 的区别

- 直接赋值：对象的引用
- 浅拷贝：拷贝父对象，不会拷贝对象内部的子对象
- 深拷贝：完全拷贝了父对象及子对象

```python
import copy

a = [1, 2, 3, 4, ['a', 'b']]

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
# c = a.copy()
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)
a[4].append('c')

print("a =", a, id(a), id(a[4]))
print("b =", b, id(b), id(b[4]))
print("d =", c, id(c), id(c[4]))
print("d =", d, id(d), id(d[4]))
# a = [1, 2, 3, 4, ['a', 'b', 'c'], 5] 140553780402312 140553781418824
# b = [1, 2, 3, 4, ['a', 'b', 'c'], 5] 140553780402312 140553781418824
# d = [1, 2, 3, 4, ['a', 'b', 'c']] 140553780402248 140553781418824
# d = [1, 2, 3, 4, ['a', 'b']] 140553780402184 140553780402120
```

## 23 Python 垃圾回收机制

Python GC(Garbage Collection) 主要使用引用计数 (Reference Counting) 来跟踪和回收垃圾。
在引用计数的基础上，通过“标记-清除” (mark and sweep) 解决容器对象可能产生的循环引用问题；通过“分代回收” (generation collection) 以空间换时间的方法提高垃圾回收效率。

### 1) 引用计数

```c
typeof struct_object {
    int ob_refcnt;
    struct_object *ob_type;
} PyObject;

```

结构体 PyObject 是每个对象必有的内容。其中 ob_refcnt 就是作为引用计数。当一个对象有了新的引用，它的 ob_refcnt 就会增加，当引用它的对象被删除，它的 ob_refcnt 就会减少。引用计数为0，该对象生命就结束了。

```python
import sys

# 获取变量 a 所引用的对象当前的引用计数
aa = "1111111111"
print(sys.getrefcount(aa))  # 4
# getrefcount() 本身会使用引用计数加一
```

优点：简单，实时性；缺点：维护引用计数消耗资源，循环引用。

### 2) 标记-清除机制

只有容器对象才会产生循环引用的问题，列表、字典、用户自定义类的对象、元组等。

**基本思路**：先按需分配，等到没有空闲内存时，从寄存器和程序栈上的引用出发，遍历以对象为节点，引用为边构成的图，把所有可以访问的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。
上面的垃圾回收阶段，会暂停整个应用程序，等到标记-清除结束后才会恢复应用程序的运行。

### 3) 分代技术

**整体思想**：将系统中所有内存块根据其存活时间划分成不同的集合，每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减少，存活时间通过利用经过几次垃圾回收来度量。
Python 默认定义三代对象集合，索引数越大，对象存活时间越长。

## 24 Python 的列表 list

在 CPython 中，列表被实现为长度可变的数组。由对其他对象的引用组成的连续数组。

### 1) list 对象的 C 结构

```c
typeof struct {
    PyObject_VAR_HEAD
    PyObject **ob_items;
    Py_ssize_t allocated;
}
```

ob_item 是保存元素的指针数组，allocated 是 ob_item 预先分配的内存总容量。

### 2) list 的初始化

allocated 的值比 ob_size 的值大，这是为了避免每次有新元素加入 list 时都要调用 realloc 进行内存分配。

### 3) append

追加一个元素，时间复杂度为 O(1).

### 4) insert

在指定位置插入一个元素，时间复杂度为 O(n).

### 5) pop

弹出最后一个元素，时间复杂度为 O(1).

### 6) remove

移除一个指定的元素，时间复杂度为 O(n).

## 25 Python 的字典 dict

字典中的 keys(), values(), items() 3个方法的返回值不是列表，而是视图对象(view object).

```python
a = {"name": "cc"}
print(a.keys())  # dict_keys(['name'])
print(a.values())  # dict_values(['cc'])
print(a.items())  # dict_items([('name', 'cc')])
```

### 实现细节

CPython 使用伪随机探测 (pseudo-random probing) 的散列表 (hash table) 作为字典的底层数据结构。只有可哈希的对象才能作为字典的键。
Python 中所有不可变的内置类型都是可哈希的。可变类型，如列表、字典、集合，是不可哈希的。

**有序字典**：collections.OrderedDict

## 26 Python 的集合 set

Python 的内置集合类型有：

- set(): 一种可变的、无序的、有限的集合，元素是唯一的，不可变的（可哈希的）对象；
- frozenset(): 一个不可变的、可哈希的、无序的集合，元素是唯一的，不可变的哈希对象。

```python
a = frozenset(range(10))
print(a)  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
```

**实现细节**：带有空值的字典，只有键才是实际的集合元素。

添加、删除、检查元素的平均时间复杂度为 O(1), 最坏时间复杂度为 O(n).

## 27 Python 中的弱引用 weakref

Python 中垃圾回收机制是基于引用计数规则。

弱引用消除了引用循环的问题。弱引用就是一个对象指针，它不会增加它的引用计数。

```python
import weakref


class Data(object):

    def __del__(self):
        print("data.__del__", id(self))


class Node(object):
    """ This is Node Class """

    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return "Node({!r})".format(self.value)

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
        print(self._parent)
        # <weakref at 0x7fd9875ec4a8; to 'Node' at 0x7fd98ba71128>

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node("parent")
print(dir(root))
print(root.__class__)
print(Node.__dict__)
print(weakref.__file__)
print(weakref.__all__)
print(sum.__self__)
print(max.__module__)
c1 = Node("child")

root.add_child(c1)
print(c1.parent)  # Node('parent')

del root
print(c1.parent)  # None
print(Node('child').__repr__())
```

@property 可以将定义的函数当作属性访问：

- 只有 @property 表示只读
- 同时有 @property 和 @x.setter 表示可读可写
- 同时有 @property、@x.setter、@x.deleter 表示可读可写可删除

## 28 Python 的 is

Python 对象的三个基本要素：id(身份识别)、type(数据类型)、value(值)。

- is 是对比地址，比较 id 值是否相等，也就是两个对象是否为同一个实例对象，是否指向同一个内存地址；
- == 是对比值，对比两个对象的内容是否相等，默认会调用 `__eq__()` 方法。

is 也被叫做同一性运算符。

**结论**：数字类型不完全相同。字符串类型不完全相同，这个和解释器实现有关；元组、列表、字典都不相同。

## 29 read, readline 和 readlines

- read: 读取整个文件，返回的是一个字符串；
- readline: 读取下一行，使用生成器方法，适用于内存不足的场景；
- readlines: 读取整个文件到一个迭代器以供遍历。

```python
import linecache

with open("a.txt", "r") as f:
    lines = f.read()
    print(lines)
    print(type(lines))  # <class: 'str'>
    line = f.readline()
    print(type(line))  # <class: 'str'>
    while line:
        print(line)
        line = f.readline()
    lines = f.readlines()  # <class 'list'>
    print(type(lines))
    for line in lines:
        print(line)


# 随机读写文本行
text = linecache.getline("a.txt", 2)
print(text)
```

### 性能对比

- read() 最快，其功能也最简约；
- readline() 和 readlines() 在功能上类似，在内存足够的情况下，使用 readlines() 可以明显地提高执行效率。

## 30 Python 2 和 3 的区别

### 1) `__future__` 模块

Python 3.x 的一些 Python 2.x 不兼容的关键字和特性可以通过在 Python 2.x 的内置 `__future__` 模块导入，from `__future__` import *

```python
# print
# python 2.x
print "Hello World"

from __future__ import print_function

print("Hello World")

# 整数除法
# python 2.x
print 5/2  # 2

# with 用法
# python 2.x
try:
    with open("test.txt", "w") as f:
        f.write("Hello World")
finally:
    f.close()
    
from __future__ import with_statement

with open("test.txt", "w") as f:
    f.write("Hello World")
    
    
# 绝对引用，针对 python 2.4 及之前版本，引用 python 自带的 .py 文件
from __future__ import absolute_import
```

### 2) print 函数

### 3) 整除

### 4) Unicode

Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型；Python 3 中有了 Unicode(utf-8), 以及一个字节类：bytes 和 bytearray.

```python
# python 2.x
print type(unicode('this is like a python3 str type'))
# <type 'unicode'>

print type(b'byte type does not exists')
<type 'str'>

print type(bytearray(b'bytearray oddly does exist though'))
# <type 'bytearray'>

# python 3.x
print(type('strings are not utf-8'))
# <type 'str'>

print(type(b'bytes for storing data'))
# <class 'bytes'>

print(type(bytearray(b'bytearrays')))
# <class 'bytearray'>
```

### 5) xrange 模块

- Python 2 中 xrange 比 range 更快；Python 3 没有了 xrange.
- Python 3 中 range 对象的 `__contains__` 方法

```python
print(range.__contains__)  # <slot wrapper '__contains__' of 'range' objects>
```

### 6) Raising exceptions

```python
# python 2.x
raise IOError, "file error"

# python 3.x
raise IOError("file error")
```

### 7) handling exceptions

```python
# python 2.x
try:
    let_us_cause_a_NameError
except NameError, err:
    print err, '--> our error message'

# python 3.x
try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '--> our error message')
```

### 8) next() 函数和 .next() 方法

在 Python 2.7.5 中函数和方法都可以使用，Python 3 中只能用 next().

### 9) for 循环变量和全局命名空间泄漏

Python 3.x 的 for 循环变量不会再导致命名空间泄漏。

```python
# python 2.x
i = 1
print 'before: i =', i
print 'comprehension: ', [i for i in range(5)]
print 'after: i =', i
# before: i = 1
# comprehension: [0, 1, 2, 3, 4]
# after: i = 4

# python 3.x
i = 1
print('before: i =', i)
print('comprehension: ', [i for i in range(5)])
print('after: i =', i)
# before: i = 1
# comprehension: [0, 1, 2, 3, 4]
# after: i = 1
```

### 10) 比较不可排序类型

Python 3 中对不可排序类型做比较时，会抛出一个类型错误。

```python
# python 2.x
print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)
# [1, 2] > 'foo' = False
# (1, 2) > 'foo' = True
# [1, 2] > (1, 2) = False

# python 3.x
print("[1, 2] > 'foo' = ", [1, 2] > 'foo')
print("(1, 2) > 'foo' = ", (1, 2) > 'foo')
print("[1, 2] > (1, 2) = ", [1, 2] > (1, 2))
# TypeError: '>' not supported between instances of 'list' and 'str'
```

### 11) 通过 input() 解析用户输入

Python 3 把用户输入存储为一个 str 对象。

### 12) 返回可迭代对象，而不是列表

Python 3 中一些方法和函数返回可迭代对象，代替 Python 2 中的列表。如 zip(), map(), filter(), dict.keys(), dict.values(), dict.items() 等。

## 31 super init

Python 3 中可以直接使用 super().xxx 代替 super(Class, self).xxx

### 1) 单继承

```python
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print("self is {0} @A.add".format(self))
        self.n += m


class B(A):
    def __init__(self):
        super().__init__()
        self.n = 3

    def add(self, m):
        print("self is {0} @B.add".format(self))
        super().add(m)
        self.n += 3


b = B()
b.add(2)
print(b.n)
# self is <__main__.B object at 0x7f8c7fd7c320> @B.add
# self is <__main__.B object at 0x7f8c7fd7c320> @A.add
# 8
```

调用父类方法 add(self, m) 时，此时父类方法的 self 不是父类的实例，而是子类的实例。

### 2) 多继承

```python
class C(A):
    def __init__(self):
        super().__init__()
        self.n = 4

    def add(self, m):
        print("self is {0} @C.add".format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        super().__init__()
        self.n = 5

    def add(self, m):
        print("self is {0} @D.add".format(self))
        super().add(m)
        self.n += 5


print(D.mro())
d = D()
d.add(2)
print(d.n)
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# self is <__main__.D object at 0x7fd033d862b0> @D.add
# self is <__main__.D object at 0x7fd033d862b0> @B.add
# self is <__main__.D object at 0x7fd033d862b0> @C.add
# self is <__main__.D object at 0x7fd033d862b0> @A.add
# 19
```

### 3) super 是一个类

- 调用 super(), 实际上是实例化了一个 super 类。super 包含了一个 MRO 以及 MRO 中的一个类。super(a_type, obj)
- MRO 是 type(obj) 的 MRO, MRO 的那个类就是 a_type. 同时 isinstance(obj, a_type) == True
- super() 提供了一个 MRO 及 一个 MRO 中的类 C, super() 将返回一个从 MRO 中 C 之后的类中查找方法的对象，即从 MRO 的 tail 中查找。

**e.x** 有个 MRO: [A, B, C, D, E, object], 调用 super(C, A).foo()，super 只会从 C 之后查找，即: 只会在 D 或 E 或 object 中查找 foo 方法。

## 32 协程

**协程**：微线程，纤程，Coroutine.
协程由程序主动控制切换，没有线程切换的开销，所以执行效率极高。对于 io 密集型任务非常适用，对于 cpu 密集型推荐多进程+协程。

“子程序就是协程的一个特例。”

### 1) yield 表达式

```python
def test():
    print("generator start")
    n = 1
    while True:
        yield_expression_value = yield n
        print("yield_expression_value = %d" % yield_expression_value)
        n += 1


generator = test()
print(type(generator))
# <class 'generator'>

next_result = generator.__next__()
print("next_result = %d" % next_result)
# generator start
# next_result = 1

send_result = generator.send(666)
print("send_result = %d" % send_result)
# yield_expression_value = 666
# send_result = 2
```

- `__next__()` 方法：启动或恢复 generator 的执行，相当于 `send(None)`;
- `send(value)` 方法：发送值给 yield 表达式。

#### 步骤

1. 创建 generator 对象：包含 yield 表达式的函数；
2. 启动 generator: 使用生成器之前需要调用 `__next__()` 或 `send(None)`, 否则会报错。启动后，代码将执行到 yield n, 然后将 n 传递到 `generator.__next__()` 的返回值；
3. 发送值给 yield 表达式：生成器从上次中断的位置继续向下执行，直到遇到下一个 yield 就暂停。
4. 注意：步骤 2 没有执行到赋值语句，到了 3 生成器恢复执行才给赋值。

### 2) 生产者和消费者模型

```python
def consumer():
    r = "start"
    print("[CONSUMER] %s" % r)
    while True:
        n = yield r
        if not n:
            print("n is empty")
            continue
        print("[CONSUMER] Consumer is consuming %s" % n)
        r = "200 ok"


def producer(c):
    start_value = c.send(None)
    print("[PRODUCER] %s" % start_value)
    n = 0
    while n < 2:
        n += 1
        print("[PRODUCER] Producer is producing %s" % n)
        r = c.send(n)
        print("[PRODUCER] Consumer return %s" % r)

    c.close()


c = consumer()
print(type(c))
# <class 'generator'>
producer(c)
# [CONSUMER] start
# [PRODUCER] start
# [PRODUCER] Producer is producing 1
# [CONSUMER] Consumer is consuming 1
# [PRODUCER] Consumer return 200 ok
# [PRODUCER] Producer is producing 2
# [CONSUMER] Consumer is consuming 2
# [PRODUCER] Consumer return 200 ok
```

### 3) yield from 表达式

```python
# 子生成器
def test(n):
    i = 0
    while i < n:
        yield i
        i += 1


# 委派生成器
@asyncio.coroutine
def test_yield_from(n):
    print("test_yield_from start")
    yield from test(n)
    print("test_yield_from doing")  # 串行执行
    yield from test(n)
    print("test_yield_from end")


for i in test_yield_from(2):
    print(i)
# test_yield_from start
# 0
# 1
# test_yield_from doing
# 0
# 1
# test_yield_from end
```

这里，yield from 起的作用相当于：

```python
import asyncio


# @asyncio.coroutine
async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    # yield from asyncio.sleep(1.0)
    await asyncio.sleep(1.0)
    return x + y


# @asyncio.coroutine
async def print_sum(x, y):
    # result = yield from compute(x, y)
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
print("start")
loop.run_until_complete(print_sum(1, 2))
print("end")
loop.close()
# start
# Compute 1 + 2 ...
# 1 + 2 = 3
# end
```

除此之外，还帮助处理了异常。

### 4) 协程(Coroutine)

Python 3.4 新增 @asyncio.coroutine 和 yield from; Python 3.5 引入 async / await.

#### @asyncio.coroutine

- 标记了 @asyncio.coroutine 装饰器的函数称为协程函数，iscoroutinefunction() 返回 true; 调用协程函数返回的对象称为协程对象，iscoroutine() 返回 true.
- @asyncio.coroutine 将在 Python 3.10 版本中移除。

#### async / await

async / await 实际上只是 @asyncio.coroutine 和 yield from 的语法糖。

```python
import asyncio

future = asyncio.Future()


async def coro1():
    print("wait 1 second")
    await asyncio.sleep(1)
    print("set result")
    future.set_result("data")


async def coro2():
    result = await future
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([coro1(), coro2()]))
loop.close()
# wait 1 second
# set result
# data
```

await future 必须等待 future.set_result(“data”) 后才能够结束。

**其他**：async with 异步上下文管理，async for 异步迭代器。
