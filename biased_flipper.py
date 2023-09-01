import random


def coinFlip(number):
    recordList = []
    heads = 0
    tails = 0
    for i in range(number):
        flip = random.random()
        if flip < 0.65:
            print("Heads")
            recordList.append("Heads")
            heads += 1
        else:
            print("Tails")
            recordList.append("Tails")
            tails += 1
    print(str(recordList))
    print(float(recordList.count("Heads")) / number)

