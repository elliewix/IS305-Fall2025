import string
from collections import Counter
import csv

# create a headers list for a-z plus word
headers = list(string.ascii_lowercase)
# insert label to the beginning of headers
headers.insert(0, "word")
print(headers)

words = ['banana', 'halloween', 'mississippi', 'illinois']
data_rows = []
for w in words:
    # tip: for hw4 you'll need to do more here
    counted_letters = Counter(w)
    row = [0] * 26
    row.insert(0, w) # add the word
    for letter, count in counted_letters.items():
        # print(letter, headers.index(letter), count)
        row[headers.index(letter)] = count
    # print(row)
    data_rows.append(row)

print(data_rows)

with open('wordcounts.csv', 'wt', encoding='utf-8', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(data_rows)

# a few stray reminders of syntax

## determining unique values from a list

word = 'mississippi'
letters = list(word)
print(letters)
print(list(set(letters)))