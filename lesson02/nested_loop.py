# Look through each array (notice how in this case we have a nested array) and print the number ->
# of times the item we pass in is present in the nested loop

li = ["apple", "banana", "orange", 25, 12, ["apple", "pear", "pear", 12, ["apple"]]]


def how_many(in_list, item):
    count = 0
    # your code here...
    for i in in_list:
        if item == i:
            count += 1
        elif type(i) == list:
            for j in i:
                if item == j:
                    count += 1
                elif type(j) == list:
                    for k in j:
                        if k == item:
                            count += 1

    print(count)


how_many(li, "apple")  # should return 3
how_many(li, 25)  # should return 1
how_many(li, "pear")  # should return 2
