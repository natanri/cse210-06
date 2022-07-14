def remove_numbers_from_grid(self):
    """remove numbers from the grid to create the puzzle"""
    #get all non-empty squares from the grid
    non_empty_squares = self.get_non_empty_squares(self.grid)
    non_empty_squares_count = len(non_empty_squares)
    rounds = 3
    while rounds > 0 and non_empty_squares_count >= 17:
        #there should be at least 17 clues
        row,col = non_empty_squares.pop()
        non_empty_squares_count -= 1
        #might need to put the square value back if there is more than one solution
        removed_square = self.grid[row][col]
        self.grid[row][col]=0
        #make a copy of the grid to solve
        grid_copy = copy.deepcopy(self.grid)
        #initialize solutions counter to zero
        self.counter=0      
        self.solve_puzzle(grid_copy)   
        #if there is more than one solution, put the last removed cell back into the grid
        if self.counter!=1:
            self.grid[row][col]=removed_square
            non_empty_squares_count += 1
            rounds -=1
    return
