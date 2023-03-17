import csv
import json
from pprint import pprint

# Read a csv file, find all results whos name start with A
# append to a object
# create and write this new appened object to json file

laureates_beginning_with_a = []

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["name"][0] == "A":
            laureates_beginning_with_a.append(row)
with open("laureates.json", "w") as f:
    json.dump(laureates_beginning_with_a, f, indent=2)
