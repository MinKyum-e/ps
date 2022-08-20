#재귀함수로 이진 탐색

def bnSearch(arr, start, end, target):
    mid = (start + end)//2
    if start > end:
        return None
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bnSearch(arr, start, mid-1, target)
    elif arr[mid] < target:
        return bnSearch(arr, mid+1, end, target)
    

n, target = map(int, input().split())

nums = list(map(int, input().split()))


res =  bnSearch(nums, 0, len(nums)-1, target)
if res == None:
    print("x")
else:
    print(res+1)


#반복문ㅡㅇ로 탐색


def bnSearch2(arr, target, start, end):

    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
        	start = mid+1
        elif arr[mid] > target:
            end = mid-1
            
    return None
res =  bnSearch2(nums, target, 0, len(nums)-1)
if res == None:
    print("x")
else:
    print(res+1)