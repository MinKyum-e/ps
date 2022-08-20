#이진 탐색 
def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid - 1
    
    return None
    


N = int(input())
stocks = list(map(int, input().split()))
M = int(input())
asked = list(map(int, input().split()))

stocks.sort()

for i in range(M):
    result = binary_search(stocks, 0, N-1, asked[i])
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")

#계수 정렬
n = int(input())
count_list = [0]*100001
for i in input().split():
    count_list[int(i)] = 1
    
m = int(input())
for i in input().split():
    if count_list[int(i)] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")

#집합 자료형

n = int(input())
sets = set(map(int, input().split()))

m = int(input())
for i in list(map(int, input().split())):
    if i in sets:
        print("yes", end = " ")
    else:
        print("no", end=" ")