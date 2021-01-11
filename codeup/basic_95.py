# codeup basic1097

arr = [[0] * 20 for _ in range(20)]

for i in range(1, 20):
    l = list(map(int, input().split())) 
    for j in range(1, 20):
        arr[i][j] = l[j-1]

n = int(input()) 

for i in range(n):
    x, y = map(int, input().split())

    for j in range(1, 20):
        if arr[x][j] == 0:
            arr[x][j] = 1
        else:
            arr[x][j] = 0
    for j in range(1, 20):
        if arr[j][y] == 0:
            arr[j][y] = 1
        else:
            arr[j][y] = 0
    

for i in range(1, 20):
    for j in range(1, 20):
        print(arr[i][j], end=' ')
    print()