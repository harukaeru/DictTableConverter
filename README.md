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
