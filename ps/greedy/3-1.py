money = int(input())
count = 0

coin = [500, 100, 50, 10]

for c in coin:
    count += money//c
    money %= c
print(count)