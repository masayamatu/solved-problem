import itertools

n = int(input())

a = []
b = []
count = 1

a = list(map(int,input().split()))
b = list(map(int,input().split()))

permutate_a =list(itertools.permutations(a))
score=[0 for i in range(len(permutate_a))]

for i in range(len(permutate_a)):
    for j in range(n):
        if permutate_a[i][j]-b[j]>0:
            score[i] += permutate_a[i][j]-b[j]

score.sort(reverse=True)

for i in range(1,len(score)):
    if(score[i]==score[i-1]):
        count += 1
    else:
        break
        
print(count)
