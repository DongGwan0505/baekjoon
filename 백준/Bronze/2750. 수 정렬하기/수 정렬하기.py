N = int(input())
n = []
for i in range(N):
    n.append(int(input()))

for j in range(N-1):
    for i in range(N-1-j):
        if n[i] > n[i+1]:
            temp = n[i]
            n[i] = n[i+1]
            n[i+1] = temp

for k in range(N):
    print(n[k])      