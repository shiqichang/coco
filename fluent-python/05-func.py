#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import operator
import random
from functools import partial
from inspect import signature


def factorial(n):
    ''' return n! '''
    return 1 if n < 2 else n * factorial(n-1)


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


def tag(name, *content, cls=None, **attrs):
    """ 生成一个或多个 HTML 标签 """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def clip(text:str, max_len:'int > 0'=80) -> str:
    """ 在 max_len 前面或后面的第一个空格处截断文本 """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))
    print(help(factorial))
    print(dir(factorial))

    fact = factorial
    print(fact)
    print(fact(5))
    print(list(map(factorial, range(11))))

    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))

    class C: pass
    obj = C()
    def func(): pass
    print(sorted(set(dir(func)) - set(dir(obj))))  # 常规对象没有而函数有的属性

    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))

    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    print(clip.__annotations__)

    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)

    sig = signature(tag)
    bound_args = sig.bind(**my_tag)
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)

    print([name for name in dir(operator) if not name.startswith('_')])

    s = 'The time has come'
    upcase = operator.methodcaller('upper')
    print(upcase(s))
    hiphenate = operator.methodcaller('replace', ' ', '-')
    print(hiphenate(s))

    triple = partial(operator.mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))

    picture = partial(tag, 'img', cls='pic-frame')
    print(picture(src='wumpus.jpeg'))
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
