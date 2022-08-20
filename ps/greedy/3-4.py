N, K = map(int, input().split())
n = 0

while True:
    if N == 1:
        break
    
    n += N%K 
    N = (N - N%K)
    if(N == 0):
        n+=1
        N+=1
        break
    N //= K
    n+=1

print(int(n))
    