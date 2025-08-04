N, M = map(int,input().split())

n=[0]*N
for a in range (N):
    n[a] = a+1

for b in range (M):
    i, j = map(int,input().split())
    temp = n[i-1]
    n[i-1] = n[j-1]
    n[j-1] = temp

print(*n)