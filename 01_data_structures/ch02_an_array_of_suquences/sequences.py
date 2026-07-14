# overview of buit sequences
"""the most powerful sequence is a list mutable container"""
# list compresention and readibility
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
  codes.append(ord(symbol))
print(codes)
codes = [ord(symbol) for symbol in symbols]
print(codes)
# local scope within comprehention and generator
x = "ABC"
codes = [ord(x) for x in x]
print(x)
x = "ABC"
codes = [last := ord(x) for x in x]
print(last) 
# Rule 1: Never reuse the same name for the loop variable and the sequence
# Comprehensions are best used for their original purpose: transform a sequence into a new list, cleanly, in one line — not for juggling extra side variables.
# listcomps vs map and filter listcomp do the same job
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
# filter
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
# cartesian product using list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
for color in colors:
  for size in sizes:
    print((color, size))
tshirts = [(color, size)  for size in sizes for color in colors]
# generator expresion save memory because it yeilds items one by one using iterator protocol instead of building a whole list just to feed another constructor
print(tuple(ord(symbol)for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
# cartesian product using in generator expression
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
  print(tshirt)

# Tubles are not just immutable lists(we can use to as immutable list and also record with no field)
students = [
    ('Alice', 20, 'A'),
    ('Bob', 22, 'B'),
    ('Cara', 21, 'A'),
]
for student in students:
    name, age, grade = student   # unpacking — position gives meaning
    print(f'{name} is {age} years old and got grade {grade}')
"""two benefits of tubles is clarity meaning it is lengh never changes(add/remove items) and it uses  less memory
A tuple itself can never change (you can't add/remove/reassign its slots) 
but if one of its items is a mutable object (like a list), that object's contents can still change, because the tuple only holds a reference to that list, not the list's actual data."""
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
b[-1].append(99)

print(a == b)
# the most visible form of unpacking is parrarel assignment 
lax_cordinates = (33.9425, -108.504450)
latttitude, longtitude = lax_cordinates
print(latttitude)
# equivalent to writing:
# pythonlatttitude = lax_cordinates[0]
# longtitude = lax_cordinates[1]
# an elegant application is swapping the values without using a temporary variable 
a , b = b , a
# using * when calling a func
t = divmod(20, 8)
divmod(*t)
# using * to grap excess items 
# defining func parameter with * args to grap arbitrary excess arguments
x, y, *rest = range(5)
print(x, y, rest)
print(rest)# 0 1 [2, 3, 4]
c, f , d = rest
print(c,f, d)
s, *body, z, e = range(5)
print(s, body, z, e)
# slicing operations
l = [10, 20, 30, 40, 50, 60]
#     0    1    2    3    4    5    ← indices
print(l[:2]) # [10, 20]
print(l[2:]) # 30, 40, 50, 60
# slice objects  stride 
word = 'bicycle'
print(word[::3]) # bye
print(word[::-1])
# Assigning to slices
our_numbers = list(range(10))
print(our_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
our_numbers[2:5] = 99, 9.99
print(our_numbers)
del our_numbers[2:5]
print(our_numbers)
our_numbers[3::2] = 200, 300
print(our_numbers)
our_numbers[2:5] = [100]
# using + and * with sequences
initial_list = [1, 2, 3]
repeated = initial_list * 5 
print(repeated)
print(initial_list)
# both + and * create new object never change their operands
# building lists of lists
board = [["-"] * 3 for i in range(3)]
# print(board)
# a list of with three references to same list is useless
weird_board = [["-"] * 3] * 3
# print(weird_board)
weird_board[1][2] = '0'
# print(weird_board)
# Same idea, spelled out as a full loop
brand_board = []
for i in range(3):
    brand_board.append(["-"] * 3)
print(brand_board)
brand_board[1][2] = '0'
print(brand_board)
# each iteration build new row and appends it to the board only row 2 is changed 
#  Augmented assignment with sequences += and *=
# outer_list = [1,2,3,4]
# print(id(outer_list)) # 4369910656
# outer_list *= 2
# print(outer_list)
# print(id(outer_list))  # 4380314496
# the list is same object we appended items to it because list is mutable so we're referencing the same list is the memory 
# let us test the tuple 
# outer_tuble = (1,2,3,4)
# print(id(outer_tuble))
# outer_tuble *= 2      # 
# print(id(outer_tuble))  # 4373860912
# Tuple — immutable, id CHANGES
# example 2-16 riddle 
# our_t = (1,2, [1, 2])
# our_t[2] += [50, 60]
# print(our_t)
#  we get an exception, but the mutation happens anyway, TypeError: 'tuple' object does not support item assignment
"""avoid putting mutable objects in tuples this our_t[2] += [50, 60] will throw an error"""
# list.sort the sorted built-in it does not create no list while sorted creates new creates
fruits = ['mango', 'raspberry', 'apple', 'banana', 'strawberry']
print(sorted(fruits, reverse=True)) # sorted list ['apple', 'banana', 'mango', 'raspberry', 'strawberry']
print(fruits)
# Arrays
# example: creating,saving and loading large amount of array
# from array import array
# from random import random
# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fb = open('floats.bin', 'wb')
# floats.tofile(fb)
# fb.close()
# floats2 = array('d')
# fb = open('floats.bin', 'rb')
# floats2.fromfile(fb, 10**7)
# fb.close()
# print(floats[0] == floats2[0])
# print(floats[-1] == floats2[-1])
import numpy as np
a = np.arange(12)
print(a)
print(a.shape)
# deques and other queues(the class is thread-safe double ended queue designated for fast
# inserting and removing)
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
dq.appendleft(-1)
print(dq)
dq.extend([10,20,30,40])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)
