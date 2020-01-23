def solution(S):
    s1 = ""
    s2 = ""
    k = int(len(S)/2)
    for i in range(k):
        if S[i] != S[-i-1] or (S[i] == '?' and S[-i-1] == '?'):
            if S[i] == '?' and S[-i-1] == '?':
                s1 += 'a'
                s2 += 'a'
            elif S[i] == '?':
                s1 += S[-i-1]
                s2 += S[-i-1]
            elif S[-i-1] == '?':
                s1 += S[i]
                s2 += S[i]
            else:
                return "NO"
        else:
            s1 += S[i]
            s2 += S[i]
    if len(S) % 2 == 1:
        s1 += S[k]

    for i in range(len(s2)-1,-1,-1):
        s1 += s2[i]
    return s1
