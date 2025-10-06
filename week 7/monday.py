# collect numbers in groups of three
count = 0
for i in range(27):
    count += 1
    # print(count)
    if count == 3:
        # print("I found 3!")
        count = 0 # reset the counter

# now count how many groups we've found

group_count = 0
count = 0
for i in range(27):
    count += 1
    # print(count)
    if count == 3:
        group_count += 1
        # print("I found 3! making", group_count, "groups")
        count = 0 # reset the counter

# so instead of counting groups, let's collect the numbers
group_count = [] # [ [0, 1, 2], [3, 4, 5], ... ]
temp = []
for i in range(27):
    # print(group_count)
    temp.append(i)
    if len(temp) == 3: # does temp have 3 items now?
        group_count.append(temp) # collection
        temp = [] # reset

# print(group_count)

###
# what if we had a diff num not divisible by three?
group_count = [] # [ [0, 1, 2], [3, 4, 5], ... ]
temp = []
for i in range(31):
    # print(group_count)
    temp.append(i)
    if len(temp) == 3: # does temp have 3 items now?
        group_count.append(temp) # collection
        temp = [] # reset
if temp: # using truthiness to check if there's something in there
    group_count.append(temp)
# alternatively, we could redo our loop
# print(group_count)

# what if we tried to keep the logic all in one place?
with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    text = infile.read()

lines = text.splitlines()
print(lines)

coords = []
temp = []
for coord_point in lines:
    temp.append(coord_point)
    if len(temp) == 3:
        coords.append(temp) # collect
        temp = [] # reset

# print(coords)
# someting fancy....
coords = []
temp = {}
count = 0
for coord_point in lines:
    count += 1
    if count == 1:
        temp["x"] = coord_point
    elif count == 2:
        temp["y"] = coord_point
    elif count == 3:
        temp["z"] = coord_point
    if len(temp) == 3:
        coords.append(temp) # collect
        count = 0
        temp = {} # reset

# print(coords)

# and even more fun....
import json
with open('coords.json', 'wt', encoding='utf-8') as outfile:
    json.dump(coords, outfile, indent = 4)


# what if we have a variable number of items for the groups?
import random
random.seed(64)
data = [ random.randint(0,10) for _ in range(50)]
print(data)

groups = []
temp = []
# for num in data:
#     temp.append(num)
#     if num == 0:
#         # if we wanted to skip the 0...
#         temp.pop(-1) # little brutal but effective
#         groups.append(temp) # collect
#         temp = [] # reset


for num in data:
    if num == 0:
        # if we wanted to skip the 0...
        groups.append(temp) # collect
        temp = [] # reset
    else:
        temp.append(num)

# print(groups)

# let's play with the look ahead pattern
# can we detect if the next item is 0?
# let's start on 0 instead of breaking on it
groups = []
temp = []
data.append(8)
for i, current in enumerate(data):
    if i < len(data) -1 : # if not i + 1 == len(data): # less readable
        upcoming = data[i + 1] # we need to proctect this
        print(current, upcoming)
        temp.append(current)
        if upcoming == 0:
            groups.append(temp)
            temp = []
    else:
        temp.append(current)
        groups.append(temp)

print(groups)