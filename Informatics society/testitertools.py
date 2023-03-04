from itertools import product
for roll in product([0, 1, 2], repeat = 3):
    roll = list(roll)
    roll.insert(0, 0)
    print(roll)