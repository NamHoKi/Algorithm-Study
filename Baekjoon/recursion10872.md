## [문제](https://www.acmicpc.net/problem/10872)

다음 소스는 N!을 수하는 Python 함수이다.

```
def factorial(n):
    if n <= 1:
        return 0
    else:
        return factorial(n-1)*n

print(factorial(int(input())))
```

## 문제
0보다 크거나 같은 정수 N이 주어진다. 이 때, N!을 출력하는 프로그램을 작성하시오.

## 입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

## 출력
첫째 줄에 N!을 출력한다.


## 메모
1재귀함수 문제는 항상
1. 그 함수가 무엇을 수행해야하는지
2. 재귀를 멈추기 위한 조건은 무엇인지

나중에 동적계획법과 차이를 확실히 알아야 할 것 같다.
