arr = [6, 2, 5,4 , 1,8, 4, 8, 0, 4, 4, 3, 9, 8]

def quick_sort(arr, start, end):
    
    if start >= end:
        return
    
    pivot = start 
    left, right = start + 1, end
    
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
            
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
            
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
    
quick_sort(arr,0,  len(arr) - 1)
print(arr)


arr2 = [6, 2, 5,4 , 1,8, 4, 8, 0, 4, 4, 3, 9, 8]
def quick_sort2(array):
    if(len(array) <= 1):
        return array
    pivot = array[0]
    tail  = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(arr2))
print(arr2)