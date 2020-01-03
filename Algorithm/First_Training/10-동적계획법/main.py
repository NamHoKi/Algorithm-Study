import sys

def read_file():
    global p
    file_name = input('File Name : ')
    with open(file_name,'r',encoding='UTF-8') as f:
        text = f.read()
    text = text.split('\n')
    n = text[0]
    n = int(n)
    p = text[1].split()
    for i in range(0,len(p)):
        p[i] = int(p[i])
    return n

def result_print(i,j):
    if i == j:
        sys.stdout.write('A')
        sys.stdout.write(str(i))
    else:
        sys.stdout.write("(")
        result_print(i, s[i][j])
        result_print(s[i][j]+1, j)
        sys.stdout.write(")")

def matrixChanin(n):
    global s
    s = [[0] * (n+1) for i in range(n+1)]
    m = [[0] * (n+1) for i in range(n+1)]
    for r in range(1,n):
        for i in range(1,n-r+1):
            j = i + r
            m[i][j] = m[i+1][j] + p[i-1]*p[i]*p[j];
            s[i][j] = i
            for k in range(i+1,j):
                if m[i][j] >m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]:
                    m[i][j] = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                    s[i][j] = k
    result_print(1,n)

def main():
    n = read_file()
    matrixChanin(n)

main()