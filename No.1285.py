from decimal import *
import math

n = int(input())

A = []

count = 1

for i in range(n):
    A.append(int(input()))
A.sort()

for i in range(1,n):
    if A[i] - A[i-1] <= 1:
        count += 1

print(count)