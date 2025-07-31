N, X = map(int, input().split())
A = []

while len(A) < N:
    A += list(map(int, input().split()))

A = A[:N]  

for num in A:
    if num < X:
        print(num, end=' ')
