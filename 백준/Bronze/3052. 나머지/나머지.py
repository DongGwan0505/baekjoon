A = []
B = []

for _ in range(10):
    num = int(input())
    remainder = num % 42
    if remainder not in B:
        B.append(remainder)

print(len(B))