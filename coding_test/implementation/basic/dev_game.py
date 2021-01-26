
n,m = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장 하기 위한 맵 생성

x,y,direction = map(int, input().split())

d[x][y] = 1 # 현재 좌표 방문 처리

#전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# array = [[1,1,1,1], [1,0,0,1] , [1,1,0,1], [1,1,1,1]]

#북,동,남,서
dx = [-1,0,1,0]
dy = [0, 1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left() # 회전
    nx = x + dx[direction] # 회전한 방향의 앞
    ny = y + dy[direction]

    # 가보지 않았고 육지인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가봤거나 바다인 경우 (회전만 함)
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_left = 0 # 다시 반복을 위한 턴타임 초기화

print(count)