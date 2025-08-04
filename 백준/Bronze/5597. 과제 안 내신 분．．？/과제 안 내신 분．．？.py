n = [0]*28
for i in range (28):
    n[i] = int(input())

v = [0]*30
for i in range (30):
    v[i] = i+1

a = True
for j in range (28):
    for i in range (30):
        if i+1 == n[j]:
            a = True
            if a == True:
                target = i + 1
                v.remove(target)

print(min(v))
print(max(v))