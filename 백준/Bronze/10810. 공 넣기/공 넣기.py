N, M = map(int, input().split())
n = [0]*N
for i in range (M):
    i, j, k = map(int, input().split())
    for a in range (i-1, j, 1):
        n[a] = k
print(*n)