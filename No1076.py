#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:17:55 2020

@author: masayamatu
"""

from decimal import *


n = int(input())
ans = 0

for x in (n):
    for y in(n):
        z = n - x - y
        if (x + y + z) == n:
            ans += 1
 
 print(ans)      