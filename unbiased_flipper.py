import random


def coinFlip(number):
    recordList = []
    heads = 0
    tails = 0
    for i in range(number):
        flip = random.randint(0, 1)
        if flip == 0:
            print("Heads")
            recordList.append("Heads")
            heads += 1
        else:
            print("Tails")
            recordList.append("Tails")
            tails += 1
    print(str(recordList))

