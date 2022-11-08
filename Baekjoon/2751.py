# https://www.acmicpc.net/problem/2751 : 수 정렬하기 2

import sys

numbers = [int(sys.stdin.readline().strip()) for i in range(int(sys.stdin.readline().strip()))]

for number in sorted(numbers):
  print(number)
