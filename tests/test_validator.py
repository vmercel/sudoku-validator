"""
Unit tests for the Sudoku Validator.
"""

import unittest
import sys
import os

# Add the parent directory to the Python path so we can import sudoku_validator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sudoku_validator.validator import SudokuValidator, validate_sudoku


class TestSudokuValidator(unittest.TestCase):
    """Test cases for the SudokuValidator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.validator = SudokuValidator()
        
        # Valid complete Sudoku board
        self.valid_complete_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        
        # Valid partial Sudoku board
        self.valid_partial_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        # Invalid board with duplicate in row
        self.invalid_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 1],  # Two 1s in first row
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
    
    def test_valid_complete_board(self):
        """Test validation of a valid complete Sudoku board."""
        self.assertTrue(self.validator.is_valid_board(self.valid_complete_board))
        self.assertTrue(self.validator.is_complete(self.valid_complete_board))
        self.assertEqual(self.validator.solve_status(self.valid_complete_board), 'solved')
    
    def test_valid_partial_board(self):
        """Test validation of a valid partial Sudoku board."""
        self.assertTrue(self.validator.is_valid_board(self.valid_partial_board))
        self.assertFalse(self.validator.is_complete(self.valid_partial_board))
        self.assertEqual(self.validator.solve_status(self.valid_partial_board), 'valid')
    
    def test_invalid_board(self):
        """Test detection of invalid boards."""
        self.assertFalse(self.validator.is_valid_board(self.invalid_board))
        self.assertEqual(self.validator.solve_status(self.invalid_board), 'invalid')
    
    def test_invalid_format(self):
        """Test handling of boards with wrong format."""
        invalid_board = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(8)]  # Wrong size
        with self.assertRaises(ValueError):
            self.validator.is_valid_board(invalid_board)
    
    def test_convenience_function(self):
        """Test the convenience validate_sudoku function."""
        self.assertTrue(validate_sudoku(self.valid_complete_board))
        self.assertFalse(validate_sudoku(self.invalid_board))


if __name__ == '__main__':
    unittest.main()
