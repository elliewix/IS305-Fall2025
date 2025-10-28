import json

with open('data.json', 'rt', encoding='utf-8') as infile:
    data = json.load(infile)

print(data)

flattened = []

def flatten_this(l):
    # print("looking at", l)
    for item in l:
        if not isinstance(item, list):
            flattened.append(item)
        else:
            flatten_this(item)

flatten_this(data)
# print(flattened)

###

rules = {'a': 'x',
         'b': 'y',
         'e': 'a+b',
         'f': 'a-b',
         'g': '-e',
         'h': '+f'
        }

def apply_rules(start):
    new = ""
    for char in start:
        new += rules.get(char, char)
    if any([ key in new for key in rules]): # check if any keys remain in our string
        return apply_rules(new)
    else:
        return new

# example: a > x, ab > xy, etc. e > a+b > x+y
print(apply_rules("a(e+f)ghghab"))

