# 메모이제이션 (피보나치 수열)

d = [0] * 100000
def f(n):
    if n == 1 or n == 2:
        return 1
    
    if d[n] != 0:
        return d[n]
    else:
        d[n] = f(n-1) + f(n-2)
        return d[n]
    
print(f(10))

#DP 바텀 업
dd = [0] * 10000

dd[1] = 1
dd[2] = 1

n = 100
for i in range(3, n+1):
    dd[i] = dd[i-1] + dd[i-2]
    
print(dd[20])