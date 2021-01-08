# codeup basic1079

n = list(map(str, input().split()))

for i in n:
    if i != 'q':
        print(i)
    elif i == 'q':
        print('q')
        break