import math

k = int(input())
ans = 0

if k==0:
    ans = math.pi**2/6
    print(ans)
else:
    for i in range(1,k+1):
        ans += 1/i
    print(ans/k)
    

