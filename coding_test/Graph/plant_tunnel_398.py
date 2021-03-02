#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면 , 루트 노드를 찾을 때 까지 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수 입력
n = int(input())
parent = [0] * (n+1) # 부모 테이블 초기화

# 모든 간선 담을 리스트, 최종비용
edges = []
result = 0

# 부모 테이블 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드 좌표값 입력
for i in range(1,n+1):
    data = list(map(int, input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 정보를 추출하여 처리
for i in range(n-1):
    # 비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)