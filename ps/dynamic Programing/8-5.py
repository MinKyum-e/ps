n, m = map(int, input().split())

coins = [int(input()) for _ in range(n)]

d = [10001] * (m+1)

for i in coins:
    d[i] = 1
    
for i in range(1, m+1):
    if d[i] != 10001:
        continue
    for j in coins:
        if i < j:
            continue
        d[i] = min(d[i-j] + 1, d[i])
        
        
print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
