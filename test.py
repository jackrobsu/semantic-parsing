from collections import OrderedDict

a = dict([(1,2),(2,3),(3,4),('1','a')])
b = OrderedDict(sorted(a.items()))
print a
print dict(b)