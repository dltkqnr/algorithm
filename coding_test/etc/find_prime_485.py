import math
#에라토스테네스의 체

m , n = map(int, input().split())

array = [True for i in range(10000001)]
array[1] = 0 # 1은 소수가 아님

for i in range(2,int(math.sqrt(n)) + 1 ): # 2부터 n의 제곱근까지의 모든 수 확인
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i 를 제외한 i의 모든 배수 제거
        j = 2
        while i * j <=  n:
            array[i*j] = False
            j += 1

# M부터 N까지의 모든 소수 출력
for i in range(m,n+1):
    if array[i]:
        print(i)
