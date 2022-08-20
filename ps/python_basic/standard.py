#1. 내장함수          :print(), input(), sorted()
#2.itertools         :순열, 조합
#3.heapq             :힙 지원, 우선순위 큐
#4. bisect           :이진탐색
#5. collections      :덱, 카운터
#6. math             :팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, pi
#7. 유용한 것         : 문자 -> 아스키 넘버, 스택 최상단 원소부터 출력 

#1
result = sum([1, 2, 3]) #iterable 객체의 모든 원소의 합 6
print(result)

result = max([10], [12, 8], [11,55]) #파라미터가 2개이상 들어왓을때 가장 큰 값, list 하나가들어오면 lsit 내부에서 가장 큰 값, list 2개 이상이면 첫 원소 크기가 가장 큰 list
print(result)

result = eval("1 + 2 *4") #문자열 수식 계산
print(result)

result = sorted([6, 2, 3]) #오름 차순
print(result)
result = sorted([77, 4, 75], reverse = True) #내림차순
print(result)

result = sorted([('나나', 56), ("니니", 2), ("가가", 3)], key = lambda x : x[1], reverse=True) #리스트 안에 튜플이나 리스트가 존재할 때 정렬 key값 지정가능
print(result)

#2
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) #모든 순열 구하기, 클래스임
print(result)

result = list(combinations(data, 2)) #data에서 n개의 데이터를 뽑는 모든 조합 구하기, 클래스임
print(result)

result = list(product(data, repeat=2)) #2배 뽑는 모든 순열(중복 허용), 클래스임
print(result)

result = list(combinations_with_replacement(data, 2)) #2배 뽑는 모든 조합(중복 허용), 클래스임
print(result)



#3 heapq Min heap으로 구성됨 == 자동으로 오름차순 정리 O(NlogN), 최대 힙 제공 x

import heapq

def heapsort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, value)
        
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 6, 3, 4, 10, 0, 44, 2, 77])
print(result)


#최대힙
def heapsort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, -value)
        
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 6, 3, 4, 10, 0, 44, 2, 77])
print(result)

#4 bisect 이진탐색용(정렬된 배열에서 특정 원소 찾기) O(logN)

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) #정렬된 순서 유지하며 a에서 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
print(bisect_right(a, x)) #정렬된 순서 유지하며 a에서 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

#값이 특정 범위에 속하는 원소의 개수 구하기

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index

a = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7]

print(count_by_range(a, 2, 4))


#5 collections

#deque
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1) #앞에 삽입
data.append(5) #뒤에 삽입
print(data)
print(list(data))

#counter
from collections import Counter

counter = Counter(['red', 'blue', 'green', 'red', 'red', 'blue'])#iterable 객체의 원소 등장 횟수 세기
print(counter['blue'])
print(counter['red'])
print(counter)

#6
import math

print(math.factorial(5))
print(math.sqrt(5))
print(math.gcd(21, 14))
print(math.pi)
print(math.e)



#7
print(ord('a')) 

stack = []

stack.append(5)
stack.append(2)
stack.append(1)

print(stack)
print(stack[::-1])