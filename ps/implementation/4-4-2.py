N, M = map(int, input().split())

A, B, direction = map(int, input().split())

world_map = [list(map(int, input().split())) for _ in range(N)]

d = [[0] * M for _ in range(N)]

d[A][B] = 1

def rotate():
    global direction
    direction -= 1
    if(direction == -1):
    	direction = 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
        
        
count = 1
rot_cnt = 0

while True:
    rotate()
    nx = A + dx[direction]
    ny = B + dy[direction]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= M: #out of order
        rot_cnt +=1
        continue
    
    if world_map[nx][ny] != 1 and d[nx][ny] != 1:
        d[nx][ny] = 1
        A = nx
        B = ny
        rot_cnt = 0
        count+=1
        continue
    else:
        rot_cnt += 1
    
    if rot_cnt == 4:
        nx = A -dx[direction]
        ny = B -dy[direction]
        if world_map[nx][ny] == 1:
            break
        else:
            A = nx
            B = ny
            rot_cnt = 0

print(count)
print(d)
        
    