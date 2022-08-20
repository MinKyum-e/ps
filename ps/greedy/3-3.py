N, M = map(int, input().split())

smallist = []

for _ in range(N):
    row = list(map(int, input().split()))
    smallist.append(min(row))
    
smallist.sort()
print(smallist[len(smallist)-1])