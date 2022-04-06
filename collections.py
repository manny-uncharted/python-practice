# collections Counter, defaultdict, OrderedDict, namedtuple

from collections import Counter
from typing import OrderedDict
"""Counter is a dict subclass for counting hashable objects."""

a = "aaaaaaaabbbbbbbccccccdddddd"

# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(2))
# print(list(my_counter.elements()))


# Named Tuple
from collections import namedtuple
"""namedtuple is used to create immutable tuple with named fields."""
"""A Python namedtuple lets us access elements in a tuple using names/labels. To define it, we import namedtuple from Python collections module and use the namedtuple() factory function."""

Point = namedtuple('Point', ['x', 'y'])
pt = Point(1,-4)
# print(pt)
# print(pt.x, pt.y)

# OrderedDict
from collections import OrderedDict
"""OrderDict is just like a regular dictionary and remembers the order in which a value was entered"""
ordered_dict = OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
# print(ordered_dict) 

# DefaultDict
from collections import defaultdict
"""DefaultDict is a subclass of dict that calls a factory function to supply missing values in a dictionary whose key hasn't been set."""
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
# print(d['c'])


from collections import deque
"""deque is a double-ended queue, which is a generalization of stacks and queues. It has append() and pop() operations in O(1) time."""
f = deque()
f.append(1)
f.append('b')
f.append(3)
f.appendleft(4)
f.popleft()
f.extendleft([5,6,7,8])
f.rotate(-1)
print(f)
