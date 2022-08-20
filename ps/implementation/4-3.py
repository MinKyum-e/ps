#ord() 유니코드 변환

position = input()

row = int(position[1])
column = int(ord(position[0])) - int(ord('a')) + 1

result =0

step = [(-1, 2), (1, 2), (-1, -2), (1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]

for i in range(8):
    if step[i][0] + row >=1 and step[i][0] + row <= 8 and step[i][1] + column >=1 and step[i][1] + column <= 8:
        result+=1
print(result)