# with notation

with open("something.txt", 'rt', encoding='utf-8') as infile:
    print(infile.read())

# equivalent without the with notation
# traditional way
infile = open("something.txt", 'rt', encoding='utf-8')
print(infile.read())
infile.close()

## pathlib, the module

import pathlib

# the Path object is the core object for this
p = pathlib.Path("something.txt")

print(p)
print(type(p))

# we can use handy methods on p
print(p.exists())
print(p.is_dir())

# import values you look up info
print(p.name, p.parts) # cool but boring
print(p.parent, p.suffix, p.stem)
print(p.absolute())

## path objects and folders

target_dir = pathlib.Path("data")
print(target_dir)
print(target_dir.absolute())
target_dir.mkdir(exist_ok=True)

# make a file inside of that folder

make_this_file = pathlib.Path("file1.txt")
output = target_dir / make_this_file
print(output.absolute())
# say you are ready to write text to it
output.write_text("my file content")