import csv

with open('pokemon_names_and_descriptions.csv','rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(len(data)) # 980

test_case = "h3r3's some t3x1-!!11!!"
# filter and keep the text and numbers
# we can use .isalnum() to check
clean_name = ""
for char in test_case:
    # print(char, char.isalnum())
    if char.isalnum():
        clean_name += char
    print(clean_name)
# alternatively
print("".join(['p', 'i','k','a']))

name = ""
for c in ['p', 'i','k','a']:
    name += c
print(name)

# a more advanced option
# use a list comp
# clean = [c for c in test_case if c.isalnum()]
clean = "".join([c for c in test_case if c.isalnum()])

print(clean)

####

# python dict review

d = {}
# add an item
d['a'] = "apple"
d['b'] = 'banana'
print(d)
d['a'] = "apples" # change or update an item

print(d)


# looping over dicts to get content
# please use the .items() method
for key, value in d.items():
    print(key, value)

####

import string
# let's create a dictionary from a loop

numbers = list(range(5,15))
letters = string.ascii_lowercase[:10]
print(numbers)
print(letters)
# just making a kind of silly example
# make a dict with {letter: letter_content}
#                  {'a': "", 'b': 'b', 'c': "cc" etc.}
# watch this build up, so this loop lets us preview the data
# for num, char in zip(numbers, letters):
#     print(num, char * num)
#     key = char
#     value = char * num

char_data = {} #dict()
# let's now add our data into the dict
for num, char in zip(numbers, letters):
    print(num, char * num)
    key = char # remember for hw2 you need to make this the actual file name
    # which I'm not doing here, you are warned
    value = char * num
    char_data[key] = value
    print(char_data) # printing inside the for loop to watch it build up

# now we can start prepping for writing out files
import pathlib

for key, value in char_data.items():
    # print(key, value)
    p = pathlib.Path(key + '.txt')
    print(p)
    # in hw2, you would actually have a target dir to write stuff out
    # which we are skipping
    p.write_text(value)

## zooming out back to the CSV stuff,
# writing out a csv file

# to do this, you need your headers and a 2D list of data
# we're just going to practice this with our existing
# headers and data, pretending that this is new data
# the newline thing here will fix the extra line situation
# for windows computers
with open('new_data.csv', 'wt', encoding='utf-8', newline="") as outfile:
    csvout = csv.writer(outfile)
    # write the headers out, 1D list, note singular
    csvout.writerow(headers)
    # write out the data from a 2D list
    csvout.writerows(data)