#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:17:55 2020

@author: masayamatu
"""

from decimal import *
import math
import itertools
from functools import reduce
from operator import xor
import array
import copy

s = list(str(input()))
n = int(input())
arrange  = copy.copy(s)
sousa = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    sousa[i][0],sousa[i][1] = map(int,input().split())
    
for i in range(n):
    count = -1
    for j in range(sousa[i][1]-1,sousa[i][0]-2,-1):
        arrange[sousa[i][0]+count] = s[j]
        count += 1
    s = copy.copy(arrange)
print("".join(arrange))