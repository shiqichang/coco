#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import functools
import html
import numbers
import time
from collections import abc

# registry = []
registry = set()

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


# def register(func):
#     print('running register(%s)' % func)
#     registry.append(func)
#     return func


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


# @register
@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_average2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


# def clock(func):
#     @functools.wraps(func)
#     def clocked(*args, **kwargs):
#         t0 = time.perf_counter()
#         result = func(*args, **kwargs)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_lst = []
#         if args:
#             arg_lst.append(', '.join(repr(arg) for arg in args))
#         if kwargs:
#             arg_lst.append('%s=%r' % (k, w)
#                            for k, w in sorted(kwargs.items()))
#         arg_str = ', '.join(arg_lst)
#         # arg_str = ', '.join(repr(arg) for arg in args)
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
#         return result
#     return clocked


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


# @clock()
# @clock('{name}: {elapsed}s')
@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


@clock()
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


@functools.lru_cache()
@ clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@functools.singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)

    print('*' * 40, 'Calling snooze(.123)')
    for i in range(3):
        snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(factorial.__name__)

    print(fibonacci(6))


if __name__ == '__main__':
    main()
