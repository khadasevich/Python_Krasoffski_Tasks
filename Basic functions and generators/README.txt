Subtask 1

Create simple function factory add_factory using 3 different approaches:

Interactive usage example:

>>> add5 = add_factory(5)
>>> print(add5(10))
15

Subtask 2

Create function reddit for downloading popular topics from www.reddit.com using closure and generator. Do not produce a full list of topics from json output but yield single topic. E.g. reddit(sub_reddit) returns function which returns generator over titles from reddit page:

Interactive usage example:

>>> python = reddit("python")
>>> golang = reddit("golang")
>>> for title in python():  # Here json data is fetched.
...     print(repr(i))
... 
u'Porting to Python 3 book is on github'
u'An Overview of using WebSockets in Python'
>>> for title in golang():  # Here json data is fetched.
...     print(title)
... 

Note 1: use following url http://www.reddit.com/r/python.json for getting subreddit information in json format.

Note 2: to limit number of topics for printing you can use itertools module: itertools.islice(golang(), 5).
Subtask 3

Create function planify and generator planify2 to expand a nested sequence.

For example, you have nested sequences such as list, tuple, MyList:

class MyList(list):
    def __str__(self):
        return "<MyList>"

seq = ('abc', 3, [8, ('x', 'y'), MyList(xrange(5)), [100, [99, [98, [97]]]]])
print(planify(seq))
# ['abc', 3, 8, 'x', 'y', 0, 1, 2, 3, 4, 100, 99, 98, 97]
gen = planify2(seq)
print(type(gen))
# <type 'generator'>
print(list(gen))
# ['abc', 3, 8, 'x', 'y', 0, 1, 2, 3, 4, 100, 99, 98, 97]

Note 1: let's take the possible depth of nesting no more than 100.
Subtask 4

Make a generator izip_repeat(*iters) that aggregates elements from each of the iterables (sequences). If the iterables are of uneven (short) length, missing values are filled-in with elements of iterable started with beginning.

See usage examples bellow:

print(list(izip_repeat([0, 1, 2], 'mn')))
# [(0, 'm'), (1, 'n'), (2, 'm')]
print(list(izip_repeat('ABCD', 'xy')))
# [('A', 'x'), ('B', 'y'), ('C', 'x'), ('D', 'y')]
print(list(izip_repeat('xy', ['mn', 'op'] , range(5))))
# [('x', 'mn', 0), ('y', 'op', 1), ('x', 'mn', 2), ('y', 'op', 3), ('x', 'mn', 4)]

Moreover, make sure you created a generator not function:

import types
g = izip_repeat('ab', [0, 1])
print(type(g))
# <type 'generator'> or <class 'generator'> for Python3
isinstance(g, types.GeneratorType)
# True
