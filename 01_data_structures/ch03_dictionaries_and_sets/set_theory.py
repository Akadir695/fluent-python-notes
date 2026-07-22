# sets are collection of unique objects. we use remove duplicate items 
l = ["spam", "spam", "spam", 'eggs', 'eggs', 'meat', 'vegs']
our_unique_items = set(l)
print(our_unique_items) # {'spam', 'eggs', 'vegs', 'meat'} 
# set literals
s = {1}
print(type(s)) # <class 'set'>
s.pop()
print(s) # set()
"""A set comprehension can be written as {expression for item in iterable [if condition]}.
we can’t create an empty set with a literal because a pair of curly braces {} represents an empty dictionary, not a set. To create an empty set, you must use the set() constructor.
Adding elements to set may change the order of existing elements"""
matrix = [
[9, 3, 8, 3],
[4, 5, 2, 8],
 [6, 4, 3, 1],
 [1, 0, 4, 5],
]
our_values = {value**2 for row in matrix for value in row}
print(our_values)
our_number = set([10, 20, 30, 30, 40, 50, 60])
print(our_number)
squared_number = {n*n for n in our_number} 
print(squared_number) # {1600, 2500, 100, 900, 3600, 400}