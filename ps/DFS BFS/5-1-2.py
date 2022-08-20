N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]


count = 0

def dfs(x, y):
    
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] != 1:
        graph[x][y] = 1
        
        dfs(x + 1, y)
        dfs(x -1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(i, j)
            count+=1

print(count)
    