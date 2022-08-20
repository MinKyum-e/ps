
n, target = map(int, input().split())

arr = list(map(int, input().split()))

print(arr)
start = 0
end = max(arr)

maximum_H = None

while start <= end:
    H = (start + end) // 2
    length = sum(list(map(lambda x : x - H, [y for y in arr if y >= H])))
    if length >= target:
        maximum_H = H
        start = H+1
    else:
        end = H-1

print(maximum_H)
        
        
        