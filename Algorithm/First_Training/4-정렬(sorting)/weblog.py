from operator import itemgetter

def m_change(m):
    if m == 'Jan':
        return 1
    elif m == 'Feb':
        return 2
    elif m == 'Mar':
        return 3
    elif m == 'Apr':
        return 4
    elif m == 'May':
        return 5
    elif m == 'Jun':
        return 6
    elif m == 'July':
        return 7
    elif m == 'Aug':
        return 8
    elif m == 'Sep':
        return 9
    elif m == 'Oct':
        return 10
    elif m == 'Nov':
        return 11
    else:
        return 12

# 파일 읽어오기
def read_file(file_name):
    global check,list
    list,ip,time,url,status = [],[],[],[],[]
    d,y,m,h,mi,s = [],[],[],[],[],[]
    check = 0
    with open(file_name, 'rt', encoding='UTF8') as f:
        lines = f.read().split('\n')
    for i in range(1,len(lines)):
        token = lines[i].split(',')
        ip.append(token[0])
        time.append(token[1][1:])
        url.append(token[2])
        status.append(token[3])
    for i in range(0,len(time)):
        d.append(time[i][:2])
        moon = time[i][3:6]
        m.append(m_change(moon))
        y.append(time[i][7:11])
        h.append(time[i][12:14])
        mi.append(time[i][15:17])
        s.append(time[i][18:])
    list = [ip,time,url,status,d,m,y,h,mi,s]

def my_print():
    global check,list
    if check == 0:
        for i in range(0, 10000):
            print(list[0][i],list[1][i],list[2][i],list[3][i])
    elif check == 1:
        for i in range(0, 10000):
            print(list[1][i])
            print('     IP:',list[0][i])
            print('     URL:', list[2][i])
            print('     Status:', list[3][i])
    else:
        for i in range(0, 10000):
            print(list[0][i])
            print('     Time:',list[3][i])
            print('     URL:', list[2][i])
            print('     Status:', list[1][i])

def sort_time():
    global list,check
    check = 1
    # for i in range(9,4,-1):
    #     list.sort(key=lambda element: element[i])

def sort_ip():
    global list,check
    sort_time()
    check = 2
    # list.sort(key=lambda element: element[0])

def main():
    while True:
        command = input('$ ')
        token = command.split()
        if token[0] == 'read':
            read_file(token[1])
        elif token[0] == 'print':
            my_print()
        elif token[0] == 'sort':
            if token[1] == '-t':
                sort_time()
            elif token[1] == '-ip':
                sort_ip()
            else:
                print('input error !')
        elif token[0] == 'exit':
            break
        else:
            print('input error !')
main()