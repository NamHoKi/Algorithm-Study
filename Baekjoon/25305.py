n, target = map(int, input().split())
scores_arr = list(map(int, input().split()))
scores_arr = sorted(scores_arr)

print(sorted(scores_arr)[-target])
