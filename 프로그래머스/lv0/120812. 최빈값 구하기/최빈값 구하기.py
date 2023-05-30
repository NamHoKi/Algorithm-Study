from collections import Counter

def solution(array):
    d = Counter(array)
    a = sorted(d, key=lambda x: d[x], reverse=True)
    if len(a) == 1 :
        return a[0]
    if d[a[0]] == d[a[1]] :
        return -1
    return a[0]