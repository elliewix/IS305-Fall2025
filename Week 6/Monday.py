# while loops

# the simplest while loop
# while True:
#     print("still going")

word = "hello"
i = 0
while i < len(word):
    print(word[i])
    i += 1

# the more pythonic way
for c in word:
    print(c)

# what if we changed it to <= instead?
# you'll get an error about index out of range
# word = "hello"
# i = 0
# while i <= len(word):
#     print(word[i])
#     i += 1

# detect the position of something unknown

text = "here's some TeXt for you"
# sentinel variables
i = 0
found = False # sentinel
while i < len(text):
    character = text[i] # first, access content
    if character == "X": # check if we've found it
        found = True
    # print(found, i, character)
    i += 1 # increment up the index

# that finds it but doesn't stop the index position
i = 0
# found = False # sentinel
# while i < len(text):
#     character = text[i] # first, access content
#     if character == "X": # check if we've found it
#         found = True
#     else: # only increment while not found
#         i += 1 # increment up the index
# print("from line 47", i)
# oops an infinite loop
found = False # sentinel
i = 0
while (not found) and i < len(text):
    character = text[i] # first, access content
    if character == "X": # check if we've found it
        found = True
    else: # only increment while not found
        i += 1 # increment up the index
print("from line 57", i)

# what if we used a True sentinel

i = 0
searching = True
while searching:
    character = text[i]
    print(character)
    if character == "X":
        searching = False
    else:
        i += 1
print("searching", i)

# my jerk way of doing this

searching = True
i = 0
while searching:
    character = text[i]
    if character == "X":
        break
    i += 1
print("from 81", i)


# we want the index position of X
print(text.index('X')) # 14

# most of the previous patterns and likely to give an error
# if the content isn't found. checking len() also needed

text = "haha no upper x here"
i = 0
while searching and i < len(text):
    character = text[i]
    if character == "X":
        searching = False
        break
    i += 1
print("97 found", i, searching)

# we can also use this is mock simulations
