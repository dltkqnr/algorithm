
n = int(input())

datas = []

for _ in range(n):
    datas = input().split()
    data[1:] = list(map(int, data[1:]))
    datas.append(data)

def setting(data):
    return -data[1], data[2], -data[3], data[0]

result = sorted(datas, key=setting)

for i in result:
    print(i[0])


