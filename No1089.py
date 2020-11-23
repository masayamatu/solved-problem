#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:17:55 2020

@author: masayamatu
"""

from decimal import *


n = int(input())
ans = 0

for x in range(n+1):
    for y in range(n+1-x):
        z = n - x - y
        if (z < 0) or (z > n):
            continue
        elif(x + y + z) == n:
            ans += 1
 
print(ans)      