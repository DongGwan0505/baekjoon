N, M = map(int, input().split())
n=[1]*N

for a in range (N):
    n[a]=(a+1)

for a in range(M):
    i, j = map(int, input().split())
    n[i-1:j] = n[i-1:j][::-1]

print(*n)