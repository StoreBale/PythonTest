def solve_queen(n):
    board = [-1] * n
    solutions = []

    def is_valid(row, col):
        for r, c in enumerate(board[:row]):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def backtrack(row=0):
        if row == n:
            solutions.append(board.copy())
            return True
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
        board[row] = -1
        return False
    
    backtrack()
    
    print(f"Total number of solutions: {len(solutions)}\n")
    
    for i, sol in enumerate(solutions):        
        print(f"Solution #{i+1}:")
        
        # Print chessboard representation of solution       
        for row in range(n):            
            line = ""
            for col in range(n):                
                line += "Q " if sol[row]==col else ". "
                
            print(line)
            
print("Solving 8 Queens problem...\n")            
solve_queen(8)