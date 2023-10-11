import json
import random

randint = random.randint(3000, 4000)

with open("penguins.json", "r") as f:
    data = json.load(f)

species = []

for i in data:
    if i["Species"] in species:
        continue
    else:
        species.append(i["Species"])


print(species)

test_list = []
data_dict = {}
for i in species:
    data_dict[i] = []

# data_dict[i].append(0)

# for i in data:
#     # print(i)
#     for j in data_dict:
#         if i["Species"] == j:
#             # data_dict[j].append(i["Body Mass (g)"])
#             test_list.append(i["Body Mass (g)"])
#             # print(data_dict)
#             print(test_list)


for i in data_dict:
    for j in data:
        if j["Body Mass (g)"] == None:
            j["Body Mass (g)"] = randint
            # print(j["Body Mass (g)"])
        if j["Species"] == i:
            data_dict[i].append(j["Body Mass (g)"])


print(data_dict)
# print(data_dict["Gentoo"][0])


"""
Assignment: 

"""
