# placing an item in a specific position
l = [4, 8, 0,8,5,5,8,5]
# say I want to put 10 in here, but at the start
# were used to append
# we need to use a diff method, insert!
l.insert(0, 10)
print(l)

# reassignment of content in a list

change_this_i = 3 # change the 3th item
l[change_this_i] = 999 # reassignment within a list
print(l)

# indexing on 2D lists

# m = [[0].copy() * 5].copy() * 5 # irrelevant to hw syntax
# just making a 5x5 matrix
m = []
[m.append([0] * 5) for _ in range(5)]
m[2][1] = 999 # row 2th col 1th change the value
for row in m:
    print(row)

# change the 0, 1 for rows 2,3...
zeroth = 8888
oneth = 7777
# this may or may not be similar to a certain inner loop
# that you need to do for a certain homework
for i in [2,3]:
    m[i][0] = zeroth
    m[i][1] = oneth

for row in m:
    print(row)