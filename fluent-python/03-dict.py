#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import builtins
from collections import ChainMap
from collections import Counter
from collections import UserDict
from unicodedata import name
from types import MappingProxyType


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item



if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'], d[4])
    print(d.get('2'), d.get(4), d.get(1, 'N/A'))
    print(2 in d, 1 in d)

    pylookup = ChainMap(locals(), globals(), vars(builtins))
    print(pylookup)

    ct = Counter('abracadabra')
    print(ct)
    ct.update('aaaaazzz')
    print(ct)
    print(ct.most_common(2))

    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    print(d_proxy[1])
    d[2] = 'B'
    print(d_proxy)
    print(d_proxy[2])

    print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
