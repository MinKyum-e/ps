#큰 수의 법칙

N, M, K = map(int, input().split())
result = 0

numbers = list(map(int, input().split()))
numbers.sort()

first = numbers[N-1]
second = numbers[N-2]

while True:
    for i in range(K):
        if M == 0:
            break
        M -=1
        result += first
    if M == 0:
        break
    result += second
    M -=1

print(result)
        
   	
    