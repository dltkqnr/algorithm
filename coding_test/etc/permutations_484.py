import itertools

data = [1,2,3,4]

# 1부터 4까지의 수 중에서 2개를 뽑아 한줄로 세우는 모든 경우를 구하는 코드
for x in itertools.permutations(data,2):
    print(list(x))

data1 = [1,2,3]

for x in itertools.combinations(data1,2):
    print(list(x), end=' ')
