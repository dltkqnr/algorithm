
n = int(input())

array = input().split()
sum = 0

for i in range(n):
    if int(array[i]) % 5 == 0:
        sum += int(array[i])

print(sum)