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

