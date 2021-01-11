# codeup basic1093

n = int(input())
m = list(map(int, input().split()))

z = [0 for i in range(23)]

for i in range(n):
    z[int(m[i])-1] += 1

for i in range(0,23):
    print(z[i], end=" ")