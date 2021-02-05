# codeup basic1065

a,b,c = map(int, input().split())
cal = [a,b,c]

for i in range(len(cal)):
    if cal[i]%2 == 0:
        print(cal[i])