# itertools: product, permutations, combinations, combinations_with_replacement, accumulate, groupby, and infinite iterators

"""Iters module used for handling iterators that can be used in a for loop"""

# Product
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=2)
# print(list(prod)) 

# Permutations
from itertools import permutations
"""permutations(iterable, r=None) returns successive r length permutations of elements in the iterable."""
c = [1,2,3]
perm = permutations(c, 2)
# print(list(perm))

# Combinations
from itertools import combinations, combinations_with_replacement
d = [1,2,3,4,5]
comb = combinations(d, 2)
# print(list(comb))

comb_wr = combinations_with_replacement(d, 2)
# print(list(comb_wr))

# Accumulate
from itertools import accumulate
import operator
"""Accumulate(iterable, func=operator.add) returns an iterator that yields the accumulated results of applying func() to the items in the iterable."""

f= [1,2,3,4,5]
# acc = accumulate(f, func=operator.mul)
acc = accumulate(f, func=max)
# print(list(acc))

# Groupby
from itertools import groupby
"""groupby(iterable, key=None) returns an iterator of grouped elements. The value returned by the iterator is a tuple of the key value and the group."""
# def smaller_than_3(x):
#     return x < 3
  
persons = [
    {'name': 'John', 'age': 20},
    {'name': 'Bob', 'age': 25},
    {'name': 'Mary', 'age': 18},
    {'name': 'Jill', 'age': 21},
]

g = [1,2,3,4,5]
# group_obj = groupby(g, key=smaller_than_3)
# group_obj = groupby(g, key=lambda x: x<3)
group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value))

# Count, cycle, repeat
from itertools import count, cycle, repeat
k = [1,2,3,4,5]

"""count(start=0, step=1) returns an iterator that counts its starting value, and increments by step, each time it is iterated."""
# for i in count(10):
#     print(i)
#     if i == 15:
#         break

"""cycle iterates through an iterable, indefinitely."""
for i in cycle(k):
    print(i)
    if i == 5:
        break