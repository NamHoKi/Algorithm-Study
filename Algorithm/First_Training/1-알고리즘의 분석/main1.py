    global exp_list
    global size
    word_list = []  # 단어 이름이 담길 리스트
    type_list = []  # 품사가 담길 리스트
    exp_list = []  # 설명이 담길 리스트
    size = 0  # 단어 수
    with open(file_name, 'rt', encoding='UTF8') as f:
        lines = f.readlines()  # 한 라인씩 읽어와서 lines(리스트)에 저장
    for i in range(0, len(lines)):
        if len(lines[i]) > 2:
            word1 = lines[i].split(' (')  # 처음 ' (' 기준 split
            word2 = lines[i].split(') ')  # 처음 ') ' 기준 split
            word_list.append(word1[0])  # 단어이름을 word_list에 순서대로 저장
            type_list.append(lines[i][len(word1[0]) + 1:len(word2[0]) + 1])  # 품사 저장
            exp_list.append(lines[i][len(word2[0]) + 2:])
            size += 1
    print('File read success.')

#중복되는 단어 개수세는 함수
def overlap_count(fi):        # if:index , m:처음 index 보다 밑에 있는 같은 단어 개수 , p:처음 index 보다 위에 있는 같은 단어 개수
    global word_list
    global size
    m = 0
    p = 0
    cnt = 1
    if fi != 0:
        while 1:
            if word_list[fi] == word_list[fi-cnt]:
                m += 1
                cnt += 1
            else:
                cnt = 1
                break
    if fi != size - 1:
        while 1:
            if word_list[fi] == word_list[fi+cnt]:
                p += 1
                cnt += 1
            else:
                cnt = 1
                break
    return [m,p]

#단어가 있을때 출력
def found_print(findex):
    global word_list
    global type_list
    global exp_list
    mp = overlap_count(findex)  # 중복단어 개수 및 index 얻기
    if mp[0] == 0 and mp[1] == 0:
        print(word_list[findex],type_list[findex],exp_list[findex])
    else:
        print('Found', mp[0] + mp[1] + 1, 'items\n')
        for a in range(findex - mp[0], findex):
            print(word_list[a], type_list[a], exp_list[a])
        for b in range(findex, findex + mp[1] + 1):
            print(word_list[b], type_list[b], exp_list[b])

#단어가 없을때 출력
def unfound_print(findex):
    global word_list
    global type_list
    global exp_list
    global size
    print('Not found.')
    if findex == -1:
        print('- - -')
        print(word_list[0], type_list[0])
    elif findex == -2:
        print(word_list[size-1], type_list[size-1])
        print('- - -')
    else:
        print(word_list[findex+1], type_list[findex+1])             # find 함수에서 단어가 없으면, return 값이 findex-1 이기 때문
        print('- - -')
        print(word_list[findex+2], type_list[findex+2])

#find 함수
def find(fword , findex , c):                                         # fword : 찾을 단어 findex : word_list 의 리스트 index
    global word_list
    global type_list
    global exp_list
    global size
    result = 0                                      # return 값 담을 변수
    if fword == word_list[findex]:                  # 찾으면
        return findex
    if findex == 0:                                              # 바로 앞 단어가 없을때, 제일 앞까지 왔을때,
        return -1
    elif findex == size-1:                                         # 제일 마지막 단어까지도 아닐때,
        return -2
    elif fword > word_list[findex] and fword < word_list[findex + 1]:  # 단어가 없을때,
        return findex-1
    else:
        up = int(findex + ((size-1)/pow(2,c)))
        down = int(findex - ((size-1)/pow(2,c)))
        if fword > word_list[findex]:
            result += find(fword, up,c+1)
        else:
            result += find(fword, down,c+1)
    if result > 0:
        return result
    else:
        return 0

#명령어 받는 함수
def process_command():
    global size
    global word_list
    while 1:
        command = input('$ ')
        token = command.split(' ')                          # token[0] : 명령어
        if command == 'exit':
            break
        elif token[0] == 'read':
            read_file(token[1])
        elif command == 'size':
            print(size)
        elif token[0] == 'find':
            if len(token) > 2:                              # 단어가 2단어 이상일때, 합쳐주기 => token[1] : 찾는 단어
                for j in range(2,len(token)):
                    token[1] = token[1] + ' ' + token[j]
            token[1] = token[1].lower()                     # 소문자로 만들기
            token[1] = token[1].capitalize()                # 첫글자만 대문자로 만들기
            findex = find(token[1], 1+ int(size/2),2)          # find 함수의 마지막 return 값을 담을 변수
            if token[1] == word_list[findex]:
                found_print(findex)
            else:
                unfound_print(findex)
        else:
            print('Input Error!')

process_command()