d = [0] * 100

# 첫번쨰 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 6

#피보나치 함수 반복분으로 구현 ( 보텀업 )
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
    print(d[i])

print(d[n])
print(d)