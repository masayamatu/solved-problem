from decimal import *
import math
import itertools
from functools import reduce
from operator import xor
import array
import copy

n = int(input())
d = []

for i in range(n):
    d.append(int(input()))

for i in range(n):
    if d[i]==1:
        print(10)
    else:
        print(9*10**(d[i]-1))

