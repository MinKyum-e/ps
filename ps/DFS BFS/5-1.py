N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]  # 공백 없을 떄 입력 잘 받기

def dfs(x, y):
    if x <= -1 or x >= N or y <=-1 or y >= M:
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1
        
        dfs(x -1, y)
        dfs(x +1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count+=1
print(count)

#15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111