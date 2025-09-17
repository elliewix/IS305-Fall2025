letters = list("here's some text")
print(letters)

print(list(enumerate(letters)))

for pair in enumerate(letters):
    i = pair[0]
    character = pair[1]
    print(character * i)

for i, character in enumerate(letters):
    print(character * i)

# we want to make file names that follow this pattern
# nnn-letter.txt
# eg 004-x.txt

# 1. create the file name, 2) make Path, 3) make go

for i, letter in enumerate(letters):
    print(str(i).zfill(3)) # to zfill we need to them to be str
    file_num = str(i).zfill(3)
    filename = file_num + "-" + letter + ".txt"
    # print(filename)

import pathlib

target = pathlib.Path("letter_files")
target.mkdir(exist_ok=True)

for i, letter in enumerate(letters):
    # print(str(i).zfill(3)) # to zfill we need to them to be str
    file_num = str(i).zfill(3)
    filename = file_num + "-" + letter + ".txt"
    letter_file = pathlib.Path(filename)
    print(target / letter_file)
    out = target / letter_file
    out.write_text(letter * i)

# what if we didn't want spaces in our file names?
for i, letter in enumerate(letters):
    # print(str(i).zfill(3)) # to zfill we need to them to be str
    file_num = str(i).zfill(3)
    filename = file_num + "-" + letter.strip() + ".txt"
    letter_file = pathlib.Path(filename)
    print(target / letter_file)
    out = target / letter_file
    out.write_text(letter * i)

# talking about glob

matches = target.glob("*.txt")
# print(list(matches))
# for p in matches:
#     p.unlink() # be careful with this
#
