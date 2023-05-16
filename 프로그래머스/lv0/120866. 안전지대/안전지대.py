
def solution(board):
    count = 0
    n = len(board)
    new_board = []
    new_board.append([0]*(n+2))
    for b in board: 
        new_board.append([0]+b+[0])
    new_board.append([0]*(n+2))
    answer = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(n): 
        for j in range(n): 
            if board[i][j]==1: 
                for x in range(i, i+3): 
                    for y in range(j, j+3): 
                        answer[x][y] +=1
                        
    # print('---------')
    for i in answer[1:-1]:
        # print(i[1:-1])   
        for j in i[1:-1]:
            # print(j)
            if j == 0:
                count+=1
    return count