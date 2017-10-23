import random

currentValue = 0
while currentValue != 100:
    currentValue = random.randint(1,100)
    if(currentValue!=100):
        print(currentValue)
    else:
        print('The end!')