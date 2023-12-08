import json
import random

# Reading in the data
randint = random.randint(20, 40)
data = []
with open("penguins.json", "r") as f:
    data = json.load(f)

# dictionary notation
for i in data:
    print(f'Value {i["Beak Depth (mm)"]}')

# Passing in the length of the beaks to our beak_lengths list
beak_lengths = []
for i in data:
    if i["Species"] == "Adelie":
        beak_lengths.append(i["Beak Length (mm)"])

# Notice there are some None values
# print(beak_lengths)

# Average beak length for all Adelie Penguins
aggregate = 0
for length in beak_lengths:
    if length == None:
        length = randint
    aggregate = aggregate + length

adelie_beak_length_average = aggregate / len(beak_lengths)

print(
    f"The average beak length of the Penguin species Adelie is : {adelie_beak_length_average}"
)
