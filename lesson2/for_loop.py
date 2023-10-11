import random

list_of_nums = []
print(list_of_nums)
for i in range(10):
    randint = random.randint(a=1, b=100)
    list_of_nums.append(randint)
    print(list_of_nums)

print(f"List of nums: {list_of_nums}")

for i in list_of_nums:
    if i % 10 == 0:
        print(f"{i} is divisible by 10!")
    elif i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
