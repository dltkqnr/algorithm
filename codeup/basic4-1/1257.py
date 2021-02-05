
a,b = map(int, input().split())

for i in range(a,b+1):
    if not i % 2 == 0:
        print(i,end=' ')