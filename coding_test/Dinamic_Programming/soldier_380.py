
n = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 로 전환
array.reverse()
dp = [1] * (n)


# 가장 긴 증가하는 부분 수열 ( LIS ) 알고리즘
for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j] + 1)


# 열외시켜야 하는 병사의 최소 수를 출력
print(n-max(dp))
