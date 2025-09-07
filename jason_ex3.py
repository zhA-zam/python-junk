import json
import pprint

with open('shows.json') as file:
    data = json.load(file)
# load or loads can return one of the two
# 1. returns nested dictionary
# 2. list of dictionaries
print(type(data))
pprint.pprint(data)