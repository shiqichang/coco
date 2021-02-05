#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import math
from array import array
from datetime import datetime


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({} {})'.format(*components)


def main():
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(repr(v1))
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))

    brl = 1/2.43
    print(brl)
    print(format(brl, '0.4f'))
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

    print(format(42, 'b'))
    print(format(2/3, '.1%'))

    now = datetime.now()
    print(format(now, '%H:%M:%S'))
    print("It's now {:%I:%M %p}".format(now))

    print(format(v1, '.2f'))
    print(format(v1, '.3e'))


if __name__ == '__main__':
    main()
