#5
#64 90 75 34 99

n = int(input()) # input = 한줄 입력(문자열)

#공백으로 구분하여 입력
data = list(map(int, input().split()))
print(data)

#적은 수의 input 바로 지정
n,m,k = map(int, input().split())
print(n, m, k)


#input 수가 많은 경우
import sys
data = sys.stdin.readline().rstrip() #문자열 입력받기 +rstrip으로 우측 공백, 줄바꿈 제거
print(data)

print("ff" + str(123) + "hhh") #문자열 더하기만 가능

#f-string 문법
answer = 8
print(f"wdwd{answer}")