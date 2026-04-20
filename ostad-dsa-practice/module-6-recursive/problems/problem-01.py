import sys
memo = {}

def is_three_x(board):
    """বোর্ডে ৩টি 'X' মিলেছে কি না তা চেক করে"""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X': return True
        if board[0][i] == board[1][i] == board[2][i] == 'X': return True
    if board[0][0] == board[1][1] == board[2][2] == 'X': return True
    if board[0][2] == board[1][1] == board[2][0] == 'X': return True
    return False

def can_win(board_tuple):
    """বর্তমান খেলোয়াড় কি কোনোভাবে জিততে পারবে?"""
    if board_tuple in memo:
        return memo[board_tuple]
    
    board = [list(row) for row in board_tuple]
    empty_cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == '.':
                empty_cells.append((r, c))
    
    for r, c in empty_cells:
        board[r][c] = 'X'
        
        if is_three_x(board):
            board[r][c] = '.'
            continue 
        
        if not can_win(tuple("".join(row) for row in board)):
            board[r][c] = '.'
            memo[board_tuple] = True
            return True
        
        board[r][c] = '.'

    memo[board_tuple] = False
    return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    try:
        N = int(input_data[0])
    except:
        return

    idx = 1
    for i in range(1, N + 1):
        if idx + 2 >= len(input_data):
            break
        grid = input_data[idx:idx+3]
        idx += 3
        
        if is_three_x(grid):
            print(f"Game {i}: Alice")
            continue

        if can_win(tuple(grid)):
            print(f"Game {i}: Alice")
        else:
            print(f"Game {i}: Bob")

if __name__ == "__main__":
    solve()