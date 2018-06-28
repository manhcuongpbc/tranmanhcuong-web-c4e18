import csv
import json

# infile = open("test_json.json","r")
# outfile = open("cate.csv", "w")

# writer = csv.writer(outfile)

# for row in json.loads(infile.read()):
#     writer.writerow(row)
json_data=open("categories.json").read()
data = json.loads(json_data)
print("finish load")

with open('cate.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'val']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()

    for key, value in data.items():
        writer.writerow({"id":key,"val":value})