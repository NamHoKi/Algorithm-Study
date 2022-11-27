# Use Code

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
