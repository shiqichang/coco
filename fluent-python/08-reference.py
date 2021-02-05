#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)

    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print(wref)
    print(wref())
    a_set = {2, 3, 4}
    print(wref())
    print(wref() is None)
    print(wref() is None)

    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
               Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))
