# Use Code
https://uni2237.tistory.com/56

<hr>

## Step 1.
정렬하면 풀이가 쉬워지는가 ?

## Step 2.
N 개수에 따른 시간복잡도 추정

## Step 3.
공부하고 여러 문제 풀어보기 ..

<hr>

## 1. 하나의 리스트에서 모든 조합을 구하기
```
items = ['1', '2', '3', '4', '5']
from itertools import permutations
list(permutations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]

from itertools import combinations
list(combinations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
```

<hr>

## 2. 두개 이상의 리스트의 모든 조합 구하기
```
from itertools import product

items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]
list(product(*items))
# [('a', '1', '!'), ('a', '1', '@'), ('a', '1', '#'), ('a', '2', '!'), ('a', '2', '@'), ('a', '2', '#'), ('a', '3', '!'), ('a', '3', '@'), ('a', '3', '#'), ('a', '4', '!'), ('a', '4', '@'), ('a', '4', '#'), ('b', '1', '!'), ('b', '1', '@'), ('b', '1', '#'), ('b', '2', '!'), ('b', '2', '@'), ('b', '2', '#'), ('b', '3', '!'), ('b', '3', '@'), ('b', '3', '#'), ('b', '4', '!'), ('b', '4', '@'), ('b', '4', '#'), ('c,', '1', '!'), ('c,', '1', '@'), ('c,', '1', '#'), ('c,', '2', '!'), ('c,', '2', '@'), ('c,', '2', '#'), ('c,', '3', '!'), ('c,', '3', '@'), ('c,', '3', '#'), ('c,', '4', '!'), ('c,', '4', '@'), ('c,', '4', '#')]
```

<hr>

## 3. 소수 구하는 함수 (유클리드 호제법)
```
def is_prime_number(x):
  for i in range(2, int(math.sqrt(x)) + 1):
      if x % i == 0:
          return False
  return True
```

<hr>

## 4. Python 딕셔너리 정렬
```
# key 기준 정렬 후, key list 반환
dic = sorted(dic, reverse=True) # 내림차순
```

```
# key 값을 기준으로 정렬된 (key,value) 원소쌍을 가진 리스트 출력 
print(sorted(dic.items()))
```

```
# value 값을 기준으로 오름차순 정렬하여 (k, v) 리스트 반환
print(sorted(dic.items(), key=lambda x:x[1]))

# 위 값을 딕셔너리로 변환
print(dict(sorted(dic.items(), key=lambda x:x[1])))

# value 값을 기준으로 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x]))
```

<hr>

## 5. Counter ( from collections)
```
from collections import Counter
```

```
>>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})
```

```
>>> Counter("hello world")
Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

<hr>

## 6. 완전탐색 (List)
```
# BFS 큐, 반복문 : 구현이 어렵지만 속도가 빠름

# DFS 재귀호출 : 구현이 쉽지만 속도가 느림
```


<hr>

## 7. 조합 구현
### 부분집합, 리스트 내 모든 조합, 리스트 끼리 교차 

<hr>

## 8. Heap

<hr>

## 9. math

```
1. factorial(x) => x의 팩토리얼 값 출력

2. sqrt(x) => x의 제곱근 출력

3. gcd(a,b) => a 와 b의 최대공약수 출력

4. 상수 pi , e => 파이와 자연상수 출력

import math

print(math.factorial(5))   # 120
print(math.sqrt(7))        # 2.6457513110645907
print(math.gcd(21,14))   # 7
print(math.pi)              # 3.14159....93
print(math.e)               # 2.71828......45
```


## 10. 아스키코드

```
# 아스키 코드 값으로 변환
a = ord('A')

# 아스키 코드 값 -> 문자
a = chr(a)
```


## 11. 진법변환

```
# n진수 -> 10진수 : int(string, base)
print(int('111',2)) # 7
print(int('222',3)) # 26
print(int('333',4)) # 63
print(int('444',5)) # 124
print(int('555',6)) # 215
print(int('FFF',16))# 4095

```


```
# 10진수 -> 2, 8, 16 진수
print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(10))  # 0xa

# return type : String -> [2:] 슬라이싱으로 진법을 지우고 사용 가능

```


## Memo
### Kakao brain 코딩 테스트
- 그래프 공부 더 하기
- 그리디, DP 공부 더 하기
