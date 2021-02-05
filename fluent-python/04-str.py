#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import array
import locale
import os
import re
import string
import sys
from unicodedata import combining
from unicodedata import name
from unicodedata import normalize
from unicodedata import numeric

expressions = """
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
"""

my_file = open('dummy', 'w')

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1^3 + 12^3 = 9^3 + 10^3.")

text_bytes = text_str.encode('utf_8')


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())


def shave_marks(txt):
    """ 去掉全部变音符号 """
    norm_txt = normalize('NFD', txt)  # 把字符分解成基字符和组合记号
    shaved = ''.join(c for c in norm_txt if not combining(c))  # 过滤掉所有组合字符
    return normalize('NFC', shaved)


def shave_marks_latin(txt):
    """ 把拉丁基字符中的所有的变音符号删除 """
    norm_txt = normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if combining(c) and latin_base:
            continue  # 忽略拉丁基字符上的变音字符
        keepers.append(c)
        # 如果不是组合字符，那就是新的基字符
        if not combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return normalize('NFC', shaved)


if __name__ == '__main__':
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    octets = bytes(numbers)
    print(octets)

    octets = b'Montr\xe9al'
    print(octets.decode('cp1252'))
    print(octets.decode('iso8859_7'))
    print(octets.decode('koi8_r'))
    print(octets.decode('utf_8', errors='replace'))

    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', repr(value))

    ohm = '\u2126'
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(name(ohm_c))
    print(ohm == ohm_c)
    print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

    print(nfc_equal('A', 'a'))
    print(fold_equal('A', 'a'))

    for char in sample:
        print('U+%04x' % ord(char),
              char.center(6),
              're_dig' if re_digit.match(char) else '-',
              'isdig' if char.isdigit() else '-',
              'isnum' if char.isnumeric() else '-',
              format(numeric(char), '5.2f'),
              name(char),
              sep='\t')

    print('Text', repr(text_str), sep='\n  ')
    print('Numbers')
    print('  str  :', re_numbers_str.findall(text_str))
    print('  bytes:', re_numbers_bytes.findall(text_bytes))
    print('Words')
    print('  str  :', re_words_str.findall(text_str))
    print('  bytes:', re_words_bytes.findall(text_bytes))

    print(os.listdir('.'))
    print(os.listdir(b'.'))

    print(sys.maxunicode)
