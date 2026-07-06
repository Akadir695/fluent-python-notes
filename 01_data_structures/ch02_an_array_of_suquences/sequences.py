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
