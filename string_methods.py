from tkinter import Y


hello = 'hello'
# print(hello.capitalize())
# print(hello.count('l'))

x = 'hello'
y = 3

# print(x*y)

# conditions and conditional operator
x = "hello"
y = "heLlo"

print(x==y)

# print(ord('a'))
# print('a'>'Z')

# Chain conditions
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2
result4 = result1 or result2 or not result3

# print(result4)
# print(result1)
# print(result2)
# print(result3)

# If and if else statements
# x = input("Name :")

# if x == 'Tim':
#     print("You are great!")
# elif x == 'Joe':
#     print("Bye Joe")
# else:
#     print("No")


# Comprehensions
x = [x for x in range(5)]
# print(x)
y  = [[0 for x in range(100)] for x in range(5)]
# print(y)

z = [i for i in range(100) if i % 5 == 0]
# print(z)

# Generator for tuple
f = tuple(i for i in range(300) if i % 5 == 0)
# print(f)


# Unpacked Operator / *args and **kwargs
# def func(*args, **kwargs):
#     pass

# def func(x, y):
#     print(x, y)

pairs = [(1,2), (3,4), (5,6)]

# for pair in pa  

x = [1, 23, 236363, 2727, 60]
# print(*x)

def func(*args, **kwargs):
    print(args, kwargs)

# func(1,2,3,4,5,one=0, two=1)

# Map and filter
x = [1,2,3,4,5,6,7,27.38,34,533,78]
mp = map(lambda i: i * 2, x)
print(list(mp))

flt = filter(lambda i: i % 3 == 0, x)
print(list(flt))