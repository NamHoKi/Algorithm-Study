import random
import sys

global NHASH,MULTIPLIER,htable
htable = []
NHASH = 4093
MULTIPLIER = 31

class prefix(object):
    def __init__(self, pword1, pword2):
        self.pword1 = pword1
        self.pword2 = pword2
        self.suf = None
        self.sumFreq = 1

class suffix(object):
    def __init__(self,sword):
        self.sword = sword
        self.freq = 1
        self.next = None

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

for i in range(0,NHASH):        # htable을 담을 list, 전부 None 으로 초기화
    htable.append(None)

def HASH_insert(key,p):
    q = htable[key]
    if htable[key] is None:                                                 # 비어있으면 넣기
        htable[key] = Node(p)
    else:
        while(True):
            if q.data.pword1 == p.pword1 and q.data.pword2 == p.pword2:     # pword1, pword2가 같은 것이 이미 있으면 sumFreq += 1
                q.data.sumFreq += 1
                suff = q.data.suf
                while(True):                                               # suf.sword가 같은게 나오면 suf.freq += 1
                    if suff.sword == p.suf.sword:
                        suff.freq += 1
                        return True
                    else:                                                   # suf.next is None 이면 삽입
                        if suff.next is None:
                            suff.next = p.suf
                            return True
                        else:                                               # suf.next is not None 이면 suf = suf.next
                            suff = suff.next
            else:                                                           # Preifx is None 까지 검사
                if q.next is None:
                    q.next = Node(p)
                    return True
                else:
                    q = q.next

def make_key(p1,p2):
    key = 0
    for j in range(0, len(p1)):             # 두 단어를 읽어와서 h(key) 설정
        key = MULTIPLIER * key + ord(p1[j])
    for j in range(0, len(p2)):
        key = MULTIPLIER * key + ord(p2[j])
    return key % NHASH

def Markov_chain():
    #시작 단어 랜덤으로 정하기
    while(True):
        random_num = random.randrange(0,NHASH)
        if random_num is not None:
            break
    key = random_num
    p1 = htable[key].data.pword1
    p2 = htable[key].data.pword2
    sys.stdout.write(p1+' ')
    sys.stdout.write(p2+' ')
    for i in range(0,998):                                                 # 가짜 텍스트 길이 : 1000 단어
        key = make_key(p1,p2)
        random_num = random.randrange(0, NHASH)
        random_num =  random_num % htable[key].data.sumFreq
        if htable[key].data.suf is None:
            break
        suff = htable[key].data.suf
        check_sum = 0
        while(True):
            check_sum += suff.freq
            if check_sum >= random_num:
                sys.stdout.write(suff.sword+' ')
                p1 = p2
                p2 = suff.sword
                break
            else:
                suff = suff.next
    print('[end]')

def main():
    with open('HarryPotter.txt','r',encoding='UTF-8') as f:
        text = f.read().split()
    for i in range(0,len(text) - 2):
        key = make_key(text[i],text[i+1])
        s = suffix(text[i+2])
        p = prefix(text[i],text[i+1])
        p.suf = s
        HASH_insert(key,p)                                    # htable에 insert

    Markov_chain()

main()