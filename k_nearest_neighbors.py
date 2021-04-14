from math import sqrt

pria = [3, 4, 4, 1, 4]
morph = [2, 5, 1, 3, 1]
jastin = [4, 3, 5, 1, 5]

def range(n1, n2):
    range = 0
    for i, j in zip(n1, n2):
        range += (i-j)**2
    return sqrt(range)

print(range(pria, morph))
