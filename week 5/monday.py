import csv

with open('pokemon_names_and_descriptions.csv',
          'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)
    # save first row to headers
    # all remaining items go into data
    # first, *middle, last = csv.reader(infile)
    # first, *_, last = csv.reader(infile)
print(headers, len(data))

"""
get into small groups
review the data that we will be messing with
identify at least 4 things wrong with the data
(there are plenty)
be ready to discuss at 11:35
"""

# let's read though the data
bad_dex_nums = []

for row in data:
    # print(row[0], row[0].isnumeric())
    dex = row[0]
    if dex.isnumeric():
        print(dex)
    else:
        bad_dex_nums.append(dex)

print(bad_dex_nums)