dp = [0] * 30001

x = int(input())

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, x+1):
    arr = []
    if i % 5 == 0:
    	arr.append(dp[i//5] +1)
    
    if i % 3 == 0:
        arr.append(dp[i//3] + 1)
    
    if i % 2 == 0:
        arr.append(dp[i//2] + 1)
    
    arr.append(dp[i-1] + 1)
    
    dp[i] = min(arr)
    
print(dp[:x+1])
print(dp[x])