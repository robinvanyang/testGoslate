# encoding: UTF-8

import re
import codecs

file1 = open('xieqilinran.txt')
file2 = codecs.open('new.txt', 'w', 'utf-8')

p = re.compile(u'开心([\u4e00-\u9fa5])就好([\u4e00-\u9fa5])手打')


def func(m):
    return m.group(1) + m.group(2)


# print p.sub(func, file1.read().decode('utf-8'))

for line in open('xieqilinran.txt', 'r'):
    line = file1.readline()
    print p.sub(func, line.decode('utf-8'))
    file2.write(p.sub(func, line.decode('utf-8')))

file1.close()
file2.close()
