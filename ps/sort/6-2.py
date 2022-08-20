n = int(input())

array = []

for _ in range(n):
    input_d = input().split()
    array.append((input_d[0], input_d[1]))
    
array.sort(key = lambda student: student[1])

for data in array:
    print(data[0], end=" ")