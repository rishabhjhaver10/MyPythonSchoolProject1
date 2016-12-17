import os
import json

path = '/Users/risha/Downloads/project 1/Tweets/Obama/'
lst = []
for fname in os.listdir(path):
    print fname
    with open(path + fname, 'r') as f:
        data = json.load(f)       
        lst.extend(data)
        print(len(data), len(lst))
print(len(lst))

infile = open('Obama_tex.txt', 'w')

for item in lst:
    item1 = item.encode("utf-8")
    infile.write(item1)
    infile.write('\n')