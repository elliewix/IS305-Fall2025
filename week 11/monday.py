import sqlite3

# 1) create the connection
conn = sqlite3.connect('pettigrew.db')

# 2) create the cursor object

c = conn.cursor()
# there's the table called letters...
results = c.execute('SELECT * FROM letters;')
print(results)

# print(results.fetchone()) # a single tuple of results
# print(results.fetchmany(10)) # first 10 results
# for row in results.fetchmany(10):
#     print(row)
records = results.fetchall()
print(len(records))
print(records[:10])

# how do we see what the tables are?

tables = c.execute('SELECT * FROM sqlite_master WHERE type = "table";')
print(tables.fetchall())

headers = ['BoxNumber', 'FolderNumber', 'Contents', 'Date']

# print(records)

results = c.execute('SELECT FolderNumber, Contents FROM letters;')

# print(results.fetchmany(10))
small_headers = ['FolderNumber', 'Contents']
all_content = results.fetchall()
import csv

with open('reduced_letters.csv', 'wt', encoding='utf-8', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(small_headers)
    csvout.writerows(all_content)

# let's turn it around and we want to make a table from the CSV

with open('reduced_letters.csv', 'rt',encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(headers)

conn2 = sqlite3.connect('small_pettigrew.sqlite3')
c2 = conn2.cursor()

c2.execute('CREATE TABLE IF NOT EXISTS letters_small (folder text, contents text);')

c2.executemany('INSERT INTO letters_small VALUES (?, ?);', data)

conn2.commit() # needed if you make changes

results = c2.execute('select * from letters_small;')
print(results.fetchall())
conn2.close() # needed to close the file up