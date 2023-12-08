import random


for i in range(10):
    randint = random.randint(0, 100)
    if randint % 2 == 0:
        print(f"{randint} -- I'm an even number!")
    elif randint % 2 == 1:
        print(f"{randint} -- I'm an odd number!")
    # else:
    #     print(f"{randint} -- I'm an odd number!")
