n , k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 배열 a는 오름차순
b.sort(reverse=True) # 배열 b는 내림차순

# a :10 20 70 40
# b :90 80 30 10

for i in range(k):
    #A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # 불필요한 for문 방지
        break

print(sum(a)) # 합 출력
    