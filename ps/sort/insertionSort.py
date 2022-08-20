arr = [6, 2, 5,4 , 1,8, 4, 8, 0, 4, 4, 3, 9, 8]


for i in range(1, len(arr)): #range(start, end, step) step 이 -1인경우 start에서 end+1까지 1씩 감소
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)