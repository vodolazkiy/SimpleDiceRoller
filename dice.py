from random import randint
from numpy import sum


def roll(sides, modifier=0, number=1):
    diedict = {
        'Coin': 2,
        'D4': 4,
        'D6': 6,
        'D8': 8,
        'D10': 10,
        'D12': 12,
        'D20': 20,
        'D100': 100
    }
    dietype = diedict[sides]
    resultarray = []

    if dietype == 2:
        modifier = 0

    for i in range(1, number + 1):
        result = randint(1, dietype) + modifier
        resultarray.append(result)

    total = sum(resultarray)

    return [total, resultarray]
