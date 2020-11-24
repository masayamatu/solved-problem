from decimal import *
import math

n = int(input())

A = []

count = 1

for i in range(n):
    A.append(int(input()))
A.sort()

a = A[0]

for i in range(1,n):
    if A[i] - a <= 1:
        count += 1
        break
    a = A[i]

print(count)