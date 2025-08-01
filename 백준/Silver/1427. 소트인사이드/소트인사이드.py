N = int(input())  # 정수 입력
sorted_digits = sorted(str(N), reverse=True) 
result = int("".join(sorted_digits))
print(result)