arr = [6, 2, 5,4 , 1,8, 4, 8, 0, 4, 4, 3, 9, 8]

count = [0] * (max(arr) +1)

for i in range(len(arr)):
    count[arr[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')