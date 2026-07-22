# A dictcomp  builds instance by taking key:value pairs from iterable 
# exampe: 3-1 dict comprehensions 
dial_code = [
  (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States"),
]
# country_dial = {}
# for code, country in dial_code:
#   country_dial[country] = code 
country_dial = {country: code for code, country in dial_code}
print(country_dial)

# {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62, 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}
low_codes ={code: country.upper()
 for country, code in sorted(country_dial.items())
 if code < 70 
 }
print(low_codes)
# merging mapping with | this operator creates new mapping
d1 = {"a": 1,"b": 2,"c": 3,"d": 4}
d2 = {"a": 50,"b": 40, "c": 60}
print(d1| d2) # {'a': 50, 'b': 40, 'c': 60, 'd': 4} # When a key exists in both dicts, the right-hand dict's value wins.
# to update the existing mapping we use |=
dic1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dic2 = {"a": 50, "b": 40, "c": 60}
dic1 |= dic2      # Step 1: update dic1 IN PLACE (on its own line)
print(dic1)      
# the object is hashable when it is hash code never changes during it is lifetime 
# a tuble is only hashable if all its items hashable and frozenset is always hashable because every element contains must be hashable by defination
tt = (1, 2, (30, 40))
print(hash(tt))
# tl =   (1, 2, [30, 40])
# print(hash(tl)) # TypeError: unhashable type: 'list'
# build index mapping word => list of occurrences
import re
import sys
WORD_RE = re.compile(r'\w+')
index = {}
# with open(sys.argv[1], encoding='utf-8') as fb:
#   for line_no, line in enumerate(fb, 1):
#     for match in WORD_RE.finditer(line):
#       word = match.group()
#       column_no = match.start() + 1
      # location = (line_no, column_no)
      # occurrances = index.get(word, [])
      # occurrances.append(location)
      # index[word] = occurrances
      # index.setdefault(word, []).append(location)
  
# Dictionary views . values(returns the views of the values in a dict
#)
the_values = dict(a=10, b=20, c = 30)
values = the_values.values()
print(values)
print(len(values))
our_dict_list = list(values)
print(our_dict_list)
squared_values =  [n*n for n in  our_dict_list]
print(squared_values)
our_dict_list
# view object is dynamic proxy is the dict is updated you can see the changes through an existing view
the_values['z'] = 1002
print(the_values)
print(squared_values)
# set comprehention
