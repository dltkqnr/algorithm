# codeup basic1096
arr = [[0]*20 for i in range(20)]

n = int(input())

for i in range(n):
    x,y = map(int, input().split())
    arr[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(arr[i][j], end=" ")
    print()