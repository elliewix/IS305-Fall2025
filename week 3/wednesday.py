# quick ways to make a list
letters_1 = list("hello")
letters_2 = list("world")

# review the mutual index pattern
## to generate the index positions we use range
## inside a for loop

for i in range(len(letters_1)):
    l1 = letters_1[i]
    l2 = letters_2[i]
    print(l1, l2)

## the zip pattern

# print(zip(letters_1, letters_2))
# if we want to see the content
# we need to recast to a list
print(list(zip(letters_1, letters_2)))

# you can loop over the results without list()
# for something in zip(letters_1, letters_2):
#     print(something)

for left, right in zip(letters_1, letters_2):
    print(left, right)

# if you wanted to index
# print(zip(letters_1, letters_2)[3])
print(list(zip(letters_1, letters_2))[3])

# assert statements
# use assert to specify a rule
# assert (boolean condition)

assert len(letters_1) == len(letters_2)

letters_3 = list("cat")

assert len(letters_1) == len(letters_3)
