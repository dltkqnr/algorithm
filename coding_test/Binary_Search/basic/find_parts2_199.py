# 계수 정렬
# n (가게 부품 개수) 입력
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
