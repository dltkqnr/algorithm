INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 출발도시,도착도시,비용 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

# 결과
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print(0)
        else:
            print(graph[a][b], end=' ')
    print()
