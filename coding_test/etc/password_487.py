from itertools import combinations


vowels = ('a','e','i','o','u')
l , c = map(int, input().split())

array = input().split(' ')
array.sort()

# 길이가 l 인 모든 암호 조합을 확인
for password in combinations(array,l):
    # 모음의 개수 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 
    if count >= 1 and count <= l-2:
        print(''.join(password))
