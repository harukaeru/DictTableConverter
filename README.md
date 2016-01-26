# DictTableConverter
```python
>>> from collections import OrderedDict
>>> d = OrderedDict((
...             ("A",
...                 OrderedDict((("1", 'o'), ("2", 'o'), ("3", 'x'),))
...             ),
...             ("B",
...                 OrderedDict((("1", 'x'), ("3", 'o'),))
...             ),
...             ("D",
...                 OrderedDict((("1", 'x'), ("2", 'x'), ("3", 'x'),))
...             ),
...             ("E",
...                 OrderedDict((("1", 'x'), ("2", 'x'), ("3", 'x'), ("5", "x"),))
...             ),
...             ("F", OrderedDict())
...         ,))
>>> from converter import Converter
>>> c = Converter()
>>> c.convert(d=d, filename="test.csv")
################
,1,2,3,5
A,o,o,x,
B,x,,o,
D,x,x,x,
E,x,x,x,x
F,,,,

################
<_io.StringIO object at 0x101639708>
>>>
```
```python
>>> something_data = dict( ~~~~ )
>>> c = Converter(data_serialize=lambda d: "○" if d else "", dict_decomposer=converter.NumDictDecomposer)
>>> c.convert(something_data, f=open("moge.csv", 'w'))
################
,24591,24592,24593,24594,24595,24596,24597,24599,24600,24802,25187,25188,25189,25190,25191
1,○,○,○,○,○,○,○,○,○,○,○,○,○,○,○
2,○,○,○,○,○,○,○,○,○,○,,,,,
3,○,○,○,○,○,○,○,○,○,○,,,,,
4,○,○,○,○,○,○,○,○,○,○,,,,,
5,○,○,○,○,○,○,○,○,○,○,,,,,
6,○,○,○,○,○,○,○,○,○,○,,,,,
7,○,○,○,○,○,○,○,○,○,○,,,,,
8,○,○,○,○,○,○,○,○,○,○,,,,,
9,○,○,○,○,○,○,○,○,○,○,○,○,○,○,○
10,○,○,○,○,○,○,○,○,○,○,○,○,○,○,○
11,○,○,○,○,○,○,○,,,○,,,,,
12,,,,,,,,,,○,,,,,

################
<_io.StringIO at 0x10a3784c8>
```
