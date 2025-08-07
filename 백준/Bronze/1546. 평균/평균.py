N = int(input())
n = list(map(int,input().split()))
M = max(n)

for i in range(N):
    n[i] = (n[i]/M)*100

avg = sum(n)/len(n)
print(avg)