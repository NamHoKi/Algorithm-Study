# def DFS(triangle, i, j, max_depth):
#     if i == max_depth:
#         return 0
#     else:
#         return triangle[i][j] + max([DFS(triangle, i+1, j, max_depth),DFS(triangle, i+1, j+1, max_depth)])
    
def solution(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            if triangle[i][j] >= triangle[i][j + 1]:
                triangle[i - 1][j] += triangle[i][j]
            else:
                triangle[i - 1][j] += triangle[i][j + 1]

    return triangle[0][0]