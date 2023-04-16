# 실제로 여러 크기의 카드가 주어졌을 때, 어떻게 정리 할 것인가 ?
# -> 세워서 가로로 길게 정렬한 뒤 정리.
def solution(sizes):
    W, H = 0, 0
    for w, h in sizes :
        if w < h :
            w, h = h, w
        W, H = max(W, w), max(H, h)
    return W * H