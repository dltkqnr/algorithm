from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(1,n+2)] 

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [[] for _ in range(1,k+2)]
idx = 1 

def bfs(graph, start, visited):
    global idx
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
                distance[idx].append(i)
        idx += 1
        if idx > k: ## 이 부분
            break

visited = [False] * 9

bfs(graph,x,visited)

distance[k].sort()

print(distance)

if not distance[k]:
    print("-1")
else:
    for i in distance[k]:
        print(i)
