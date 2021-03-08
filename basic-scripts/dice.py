import random
import os
import time

dice = list(range(1, 7))
random.shuffle(dice)

os.system('clear')

for x in dice:
    print(x)
    for i in range(3):
        print('*')
        time.sleep(0.5)
    os.system('clear')

print(f'The number is: {random.choice(dice)}')
