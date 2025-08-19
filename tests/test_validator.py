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
        self.invalid_row_duplicate = [
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
        
        # Invalid board with duplicate in column
        self.invalid_column_duplicate = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [5, 4, 5, 2, 8, 6, 1, 7, 9]  # 5 appears twice in first column
        ]
        
        # Invalid board with duplicate in box
        self.invalid_box_duplicate = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 5, 3, 4, 2, 5, 6, 7],  # 5 appears twice in top-left box
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 8, 2, 8, 6, 1, 7, 9]
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
    
    def test_invalid_row_duplicate(self):
        """Test detection of duplicate values in a row."""
        self.assertFalse(self.validator.is_valid_board(self.invalid_row_duplicate))
        self.assertEqual(self.validator.solve_status(self.invalid_row_duplicate), 'invalid')
    
    def test_invalid_column_duplicate(self):
        """Test detection of duplicate values in a column."""
        self.assertFalse(self.validator.is_valid_board(self.invalid_column_duplicate))
        self.assertEqual(self.validator.solve_status(self.invalid_column_duplicate), 'invalid')
    
    def test_invalid_box_duplicate(self):
        """Test detection of duplicate values in a 3x3 box."""
        self.assertFalse(self.validator.is_valid_board(self.invalid_box_duplicate))
        self.assertEqual(self.validator.solve_status(self.invalid_box_duplicate), 'invalid')
    
    def test_invalid_format_wrong_size(self):
        """Test handling of boards with wrong dimensions."""
        # Wrong number of rows
        invalid_board = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(8)]
        with self.assertRaises(ValueError):
            self.validator.is_valid_board(invalid_board)
        
        # Wrong number of columns
        invalid_board = [[1, 2, 3, 4, 5, 6, 7, 8] for _ in range(9)]
        with self.assertRaises(ValueError):
            self.validator.is_valid_board(invalid_board)
    
    def test_invalid_format_wrong_values(self):
        """Test handling of boards with invalid values."""
        # Values outside 0-9 range
        invalid_board = [[10 if i == 0 and j == 0 else 0 for j in range(9)] for i in range(9)]
        with self.assertRaises(ValueError):
            self.validator.is_valid_board(invalid_board)
        
        # Non-integer values
        invalid_board = [['1' if i == 0 and j == 0 else 0 for j in range(9)] for i in range(9)]
        with self.assertRaises(ValueError):
            self.validator.is_valid_board(invalid_board)
    
    def test_empty_board(self):
        """Test validation of an empty board (all zeros)."""
        empty_board = [[0 for _ in range(9)] for _ in range(9)]
        self.assertTrue(self.validator.is_valid_board(empty_board))
        self.assertFalse(self.validator.is_complete(empty_board))
        self.assertEqual(self.validator.solve_status(empty_board), 'valid')
    
    def test_convenience_function(self):
        """Test the convenience validate_sudoku function."""
        self.assertTrue(validate_sudoku(self.valid_complete_board))
        self.assertTrue(validate_sudoku(self.valid_partial_board))
        self.assertFalse(validate_sudoku(self.invalid_row_duplicate))
        
        # Test with invalid format (should return False, not raise exception)
        invalid_board = [[1, 2, 3] for _ in range(3)]
        self.assertFalse(validate_sudoku(invalid_board))
    
    def test_get_box(self):
        """Test the _get_box method."""
        # Test top-left box (0,0)
        box = self.validator._get_box(self.valid_complete_board, 0, 0)
        expected_box = [5, 3, 4, 6, 7, 2, 1, 9, 8]
        self.assertEqual(box, expected_box)
        
        # Test center box (1,1)
        box = self.validator._get_box(self.valid_complete_board, 1, 1)
        expected_box = [7, 6, 1, 8, 5, 3, 9, 2, 4]
        self.assertEqual(box, expected_box)
        
        # Test bottom-right box (2,2)
        box = self.validator._get_box(self.valid_complete_board, 2, 2)
        expected_box = [2, 8, 4, 6, 3, 5, 1, 7, 9]
        self.assertEqual(box, expected_box)
    
    def test_is_valid_group(self):
        """Test the _is_valid_group method."""
        # Valid group with no duplicates
        valid_group = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(self.validator._is_valid_group(valid_group))
        
        # Valid group with zeros (empty cells)
        valid_group_with_zeros = [1, 2, 0, 4, 0, 6, 7, 0, 9]
        self.assertTrue(self.validator._is_valid_group(valid_group_with_zeros))
        
        # Invalid group with duplicates
        invalid_group = [1, 2, 3, 4, 5, 6, 7, 8, 1]
        self.assertFalse(self.validator._is_valid_group(invalid_group))
        
        # All zeros should be valid
        all_zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.validator._is_valid_group(all_zeros))


if __name__ == '__main__':
    unittest.main()
