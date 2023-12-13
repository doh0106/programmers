def is_sq(x, y, B):
    t = B[x][y]
    if B[x+1][y+1]==B[x][y+1]==B[x+1][y]==t:
        return True
    return False

def solution(m, n, board):
    board = [list(b) for b in board]
    answer = 0
    visited = [[False]*n for _ in range(m)]
    
    
    while True:
        check = 0
        for i in range(m-1):
            for j in range(n-1):
                if is_sq(i, j, board):
                    visited[i][j]=True
                    visited[i+1][j]=True
                    visited[i][j+1]=True
                    visited[i+1][j+1]=True


        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    board[i][j] = ' '

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if visited[i][j]:
                    temp_idx = i
                    while temp_idx > 0:
                        temp_idx -= 1
                        if not visited[temp_idx][j]:
                            visited[i][j], visited[temp_idx][j] = visited[temp_idx][j], visited[i][j]
                            board[i][j], board[temp_idx][j] = board[temp_idx][j], board[i][j]
                            check += 1
                            break
        if check == 0:
            break
    answer = sum([bb.count(' ') for bb in board])
    return answer