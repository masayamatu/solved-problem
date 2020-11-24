import itertools
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd,numbers)

n = int(input())

a = []

count = 0

for i in range(n):
    a.append(int(input()))

combinate_a=list(itertools.combinations(a,3))

for i in range(len(combinate_a)):
    if gcd(combinate_a[i][0],combinate_a[i][1],combinate_a[i][2]) == 1:
        count += 1

print(count)


