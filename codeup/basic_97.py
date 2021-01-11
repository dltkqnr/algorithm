# codeup basic1099
arr = [[0]*11 for i in range(11)]

for x in range (1,11):
    l = list(map(int, input().split()))
    for y in range(1,11):
        arr[x][y] = l[y-1]

x = 2
y = 2

while True:
    if (arr[x][y] == 2):
        arr[x][y] = 9
        break

    arr[x][y] = 9
    if(arr[x][y+1 == 1]):
        if(arr[x+1][y] == 1):
            break
        else:
            x += 1
    else:
        y += 1

for i in range(1,11):
    for j in range(1,11):
        print(arr[i][j], end=" ")
    print()


