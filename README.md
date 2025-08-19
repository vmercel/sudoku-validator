# Sudoku Validator

Validates 9x9 Sudoku puzzles according to standard rules.

## Usage

```python
from sudoku_validator import SudokuValidator

validator = SudokuValidator()
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], ...]  # 0 = empty

print(validator.is_valid_board(board))  # True/False
print(validator.solve_status(board))    # 'valid', 'solved', or 'invalid'
```

## API

- `is_valid_board(board)` - Validates Sudoku rules
- `is_complete(board)` - Checks if board is full
- `solve_status(board)` - Returns board status
- `validate_sudoku(board)` - Convenience function

## Edge Cases

Handles invalid dimensions, data types, out-of-range values, empty boards, partial boards, and all Sudoku rule violations.

**Author:** Mercel Vubangsi
