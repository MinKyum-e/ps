n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 101

dp[1] = arr[0]
dp[2] = arr[1]
dp[3] = dp[1] + arr[2]

res = 0

for i in range(4, n+1):
    dp[i] = max(dp[i-2], dp[i-3]) + arr[i-1]
    if dp[i] > res:
        res = dp[i]
    
dp2 = [0] * 101

dp2[0] = arr[0]
dp2[1] = max(arr[0], arr[1])
for i in range(2, n):
    dp2[i] = max(dp2[i-1], dp2[i-2] + arr[i])
        
print(res)
print(dp2[n-1])



