
n = int(input())

array = input().split()
count = 0

for i in range(n):
    if int(array[i]) % 2 == 0:
        count += 1

print(count)