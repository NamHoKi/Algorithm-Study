# https://www.acmicpc.net/problem/25305 <- 백준사이트 25305번: 커트라인

n, target = map(int, input().split())
scores_arr = list(map(int, input().split()))
scores_arr = sorted(scores_arr)

print(sorted(scores_arr)[-target])
