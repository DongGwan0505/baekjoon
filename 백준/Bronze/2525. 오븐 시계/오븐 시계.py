A, B = map(int, input().split())
C = int(input())

# 총 분 단위로 계산
total_minutes = A * 60 + B + C

# 다시 시, 분으로 변환
A = (total_minutes // 60) % 24
B = total_minutes % 60

print(f"{A} {B}")