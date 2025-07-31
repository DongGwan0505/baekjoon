N = int(input())

A = list(map(int, input().split()))

A = A[:N]

print(min(A), max(A))