"""
Sudoku Validator

This module provides functionality to validate 9x9 Sudoku puzzles.
"""

class SudokuValidator:
    def __init__(self):
        """Initialize the SudokuValidator."""
        pass
    
    def is_valid_board(self, board):

        if not self._is_valid_format(board):
            raise ValueError("Invalid board format. Expected 9x9 grid with integers 0-9.")
        
        return (self._validate_rows(board) and 
                self._validate_columns(board) and 
                self._validate_boxes(board))
    
    def _is_valid_format(self, board):

        if not isinstance(board, list) or len(board) != 9:
            return False
        
        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False
            for cell in row:
                if not isinstance(cell, int) or cell < 0 or cell > 9:
                    return False
        
        return True
    
    def _validate_rows(self, board):

        for row in board:
            if not self._is_valid_group(row):
                return False
        return True
    
    def _validate_columns(self, board):

        for col_idx in range(9):
            column = [board[row_idx][col_idx] for row_idx in range(9)]
            if not self._is_valid_group(column):
                return False
        return True
    
    def _validate_boxes(self, board):

        for box_row in range(3):
            for box_col in range(3):
                box = self._get_box(board, box_row, box_col)
                if not self._is_valid_group(box):
                    return False
        return True
    
    def _get_box(self, board, box_row, box_col):

        box = []
        start_row = box_row * 3
        start_col = box_col * 3
        
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                box.append(board[row][col])
        
        return box
    
    def _is_valid_group(self, group):
        # Filter out zeros (empty cells)
        non_zero_values = [val for val in group if val != 0]
        
        # Check for duplicates
        return len(non_zero_values) == len(set(non_zero_values))
    
    def is_complete(self, board):

        if not self._is_valid_format(board):
            return False
        
        for row in board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    def solve_status(self, board):

        try:
            if not self.is_valid_board(board):
                return 'invalid'
            elif self.is_complete(board):
                return 'solved'
            else:
                return 'valid'
        except ValueError:
            return 'invalid'


def validate_sudoku(board):

    validator = SudokuValidator()
    try:
        return validator.is_valid_board(board)
    except ValueError:
        return False
