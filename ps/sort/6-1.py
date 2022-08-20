N = int(input())

numbers = [int(input()) for _ in range(N)]

numbers.sort(reverse=True)

for a in numbers:
    print(a, end=" ")