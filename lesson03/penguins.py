import json
import random

randint = random.randint(3000, 4000)

with open("penguins.json", "r") as f:
    data = json.load(f)

for i in data:
    if i["Species"] in species:
        continue
    else:
        species.append(i["Species"])


# In this code block we're putting a random integer between 3000 and 4000 as a replacement for any None types
for i in data:
    for j in data:
        if j["Body Mass (g)"] == None:
            j["Body Mass (g)"] = randint
            print(j["Body Mass (g)"])
        if j["Species"] == i:
            data_dict[i].append(j["Body Mass (g)"])


print(data)
print(data["Gentoo"][0])


"""
Assignment: 
Iterate through the JSON object stored in the variable 'data' and get the average body mass of each species of penguin
"""
