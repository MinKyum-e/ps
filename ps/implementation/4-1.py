N = int(input())
command = input().split()
cx = 1
cy = 1

for i in range(len(command)):
    if command[i] == 'L' and cx-1 > 0:
        cx -=1
    elif command[i] == 'R' and cx+1 <= N:
        cx +=1
    elif command[i] == 'U' and cy-1 > 0:
        cy -=1
    elif command[i] == 'D' and cy+1 <= N :
        cy +=1
        
print(cy, cx)