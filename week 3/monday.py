l = [4, 5, 6, 7, 8]
letters = ['a', 'b', 'c', 'd', 'e']

# sequential for loops
for number in l:
    print(number)

for letter in letters:
    print(letter)

# only one and then the other
# not what we want

# next, try nested loops
for number in l:
    for letter in letters:
        print(number, letter)

# this is the cross product
# still not there

# how do we get these paired
# values but only once each?

# we can use range() to generate
# index positions

# print(range(5)) # oops, a generator
print(list(range(5))) # just use list to see the content\

# this is your mutual index pattern
index_length = len(l)
for i in range(index_length):
    print(i, l[i], letters[i])

# what if we use zip()?

print(zip("hello", "world"))
