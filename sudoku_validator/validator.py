"""
Sudoku Validator

This module provides functionality to validate 9x9 Sudoku puzzles.
"""

class SudokuValidator:
    """
    A class to validate 9x9 Sudoku puzzles.
    
    The validator checks if a completed or partially completed Sudoku puzzle
    follows the standard Sudoku rules:
    - Each row contains unique digits 1-9 (no duplicates)
    - Each column contains unique digits 1-9 (no duplicates)
    - Each 3x3 sub-grid contains unique digits 1-9 (no duplicates)
    """
    
    def __init__(self):
        """Initialize the SudokuValidator."""
        pass
    
    def is_valid_board(self, board):
        """
        Validate a complete or partial Sudoku board.
        
        Args:
            board (list): A 9x9 list of lists representing the Sudoku board.
                         Each cell should contain an integer 1-9 or 0 for empty cells.
        
        Returns:
            bool: True if the board is valid according to Sudoku rules, False otherwise.
        
        Raises:
            ValueError: If the board format is invalid.
        """
        if not self._is_valid_format(board):
            raise ValueError("Invalid board format. Expected 9x9 grid with integers 0-9.")
        
        return (self._validate_rows(board) and 
                self._validate_columns(board) and 
                self._validate_boxes(board))
    
    def _is_valid_format(self, board):
        """
        Check if the board has the correct format.
        
        Args:
            board: The board to validate.
        
        Returns:
            bool: True if format is valid, False otherwise.
        """
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
        """
        Validate all rows in the board.
        
        Args:
            board (list): The Sudoku board.
        
        Returns:
            bool: True if all rows are valid, False otherwise.
        """
        for row in board:
            if not self._is_valid_group(row):
                return False
        return True
    
    def _validate_columns(self, board):
        """
        Validate all columns in the board.
        
        Args:
            board (list): The Sudoku board.
        
        Returns:
            bool: True if all columns are valid, False otherwise.
        """
        for col_idx in range(9):
            column = [board[row_idx][col_idx] for row_idx in range(9)]
            if not self._is_valid_group(column):
                return False
        return True
    
    def _validate_boxes(self, board):
        """
        Validate all 3x3 boxes in the board.
        
        Args:
            board (list): The Sudoku board.
        
        Returns:
            bool: True if all boxes are valid, False otherwise.
        """
        for box_row in range(3):
            for box_col in range(3):
                box = self._get_box(board, box_row, box_col)
                if not self._is_valid_group(box):
                    return False
        return True
    
    def _get_box(self, board, box_row, box_col):
        """
        Extract a 3x3 box from the board.
        
        Args:
            board (list): The Sudoku board.
            box_row (int): Box row index (0-2).
            box_col (int): Box column index (0-2).
        
        Returns:
            list: A list of 9 elements representing the box.
        """
        box = []
        start_row = box_row * 3
        start_col = box_col * 3
        
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                box.append(board[row][col])
        
        return box
    
    def _is_valid_group(self, group):
        """
        Check if a group (row, column, or box) is valid.
        
        A group is valid if it contains no duplicate non-zero numbers.
        
        Args:
            group (list): A list of 9 integers.
        
        Returns:
            bool: True if the group is valid, False otherwise.
        """
        # Filter out zeros (empty cells)
        non_zero_values = [val for val in group if val != 0]
        
        # Check for duplicates
        return len(non_zero_values) == len(set(non_zero_values))
    
    def is_complete(self, board):
        """
        Check if the Sudoku board is completely filled.
        
        Args:
            board (list): The Sudoku board.
        
        Returns:
            bool: True if the board is completely filled, False otherwise.
        """
        if not self._is_valid_format(board):
            return False
        
        for row in board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    def solve_status(self, board):
        """
        Determine the status of a Sudoku board.
        
        Args:
            board (list): The Sudoku board.
        
        Returns:
            str: 'solved' if complete and valid, 'valid' if valid but incomplete,
                 'invalid' if not valid according to Sudoku rules.
        """
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
    """
    Convenience function to validate a Sudoku board.
    
    Args:
        board (list): A 9x9 list of lists representing the Sudoku board.
    
    Returns:
        bool: True if the board is valid, False otherwise.
    """
    validator = SudokuValidator()
    try:
        return validator.is_valid_board(board)
    except ValueError:
        return False
