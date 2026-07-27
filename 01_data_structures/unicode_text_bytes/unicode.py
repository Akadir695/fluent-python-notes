"""
characters, code points, byte representations
encoding for full unicode
best practices for text files
the default encoding trap (from earlier)
"""
# the identity of character is code point and the actual bytes that represent the character depend on the encodiing in use
# so we converting code point to bytes that is what is called encoding, from bytes to codepoint is decoding 
s = 'café'
print(len(s))        # 4
b = s.encode('utf8')
print(b)   
print(b.decode("utf8"))      
# BAD - relies on a hidden default
with open('cafe.txt', 'w') as f:
    f.write('café')

with open('cafe.txt') as f:
    print(f.read())
# GOOD - explicit encoding, no ambiguity
with open('cafe.txt', 'w', encoding='utf-8') as f:
    f.write('café')

with open('cafe.txt', encoding='utf-8') as f:
    print(f.read())    # 'café'
from unicodedata import name
print(name('a'))