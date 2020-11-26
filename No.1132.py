
a,b,c,d,p,q = map(int,input().split())

M , XM = -10000000000,-101
m , Xm = 10000000000,-101

for i in range (p,q+1):
    if M < a*i**3+b*i**2+c*i+d:
        M = a*i**3+b*i**2+c*i+d
        XM = i
    if m > a*i**3+b*i**2+c*i+d:
        m = a*i**3+b*i**2+c*i+d
        Xm = i

print(M,XM,m,Xm)