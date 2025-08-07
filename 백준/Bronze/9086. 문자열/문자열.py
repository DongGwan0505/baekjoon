T = int(input())
n=[]
for i in range(T):
    n.append(input())

for i in range(T):
    print(n[i][0] + n[i][-1])