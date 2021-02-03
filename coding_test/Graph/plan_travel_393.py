
# 집합 찾기
def find_parent(parent,x):
    #루트 노드 찾을 때 까지
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

# 여행지 개수, 여행 계획 속 여행지 개수
n , m = map(int, input().split())
parent = [0] * (n+1)

#부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i

# 각각 union 연산 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우
            union_parent(parent, i+1 , j+1)

# 여행 계획 입력
plan = list(map(int, input().split()))

result = True

# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m-1):
    if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 확인 ( 루트가 동일한지 )
if result:
    print("YES")
else:
    print("NO")
