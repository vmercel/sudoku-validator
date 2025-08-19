# Sudoku Validator

A Python package for validating 9x9 Sudoku puzzles according to standard Sudoku rules.

## Features

- Validate complete and partial Sudoku boards
- Check for rule violations in rows, columns, and 3x3 boxes
- Determine if a board is solved, valid but incomplete, or invalid
- Comprehensive error handling for invalid board formats
- Well-tested with extensive unit tests

## Installation

Clone this repository:

```bash
git clone https://github.com/vmercel/sudoku-validator.git
cd sudoku-validator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from sudoku_validator import SudokuValidator

# Create a validator instance
validator = SudokuValidator()

# Example Sudoku board (0 represents empty cells)
board = [
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

# Validate the board
is_valid = validator.is_valid_board(board)
print(f"Is board valid? {is_valid}")

# Check if the board is complete
is_complete = validator.is_complete(board)
print(f"Is board complete? {is_complete}")

# Get the solve status
status = validator.solve_status(board)
print(f"Board status: {status}")  # 'valid', 'solved', or 'invalid'
```

### Convenience Function

```python
from sudoku_validator import validate_sudoku

# Quick validation using the convenience function
is_valid = validate_sudoku(board)
print(f"Is board valid? {is_valid}")
```

## API Reference

### SudokuValidator Class

#### Methods

- `is_valid_board(board)`: Validates a Sudoku board according to standard rules
  - **Parameters**: `board` (list) - A 9x9 list of lists with integers 0-9
  - **Returns**: `bool` - True if valid, False otherwise
  - **Raises**: `ValueError` if board format is invalid

- `is_complete(board)`: Checks if a board is completely filled
  - **Parameters**: `board` (list) - A 9x9 list of lists with integers 0-9
  - **Returns**: `bool` - True if complete, False otherwise

- `solve_status(board)`: Determines the status of a Sudoku board
  - **Parameters**: `board` (list) - A 9x9 list of lists with integers 0-9
  - **Returns**: `str` - 'solved', 'valid', or 'invalid'

### Convenience Function

- `validate_sudoku(board)`: Quick validation function
  - **Parameters**: `board` (list) - A 9x9 list of lists with integers 0-9
  - **Returns**: `bool` - True if valid, False otherwise (no exceptions)

## Sudoku Rules

The validator checks for the following standard Sudoku rules:

1. **Rows**: Each row must contain unique digits 1-9 (no duplicates)
2. **Columns**: Each column must contain unique digits 1-9 (no duplicates)
3. **Boxes**: Each 3x3 box must contain unique digits 1-9 (no duplicates)

Empty cells are represented by 0 and are ignored during validation.

## Board Format

Boards should be provided as a 9x9 list of lists where:
- Each cell contains an integer from 0-9
- 0 represents an empty cell
- 1-9 represent filled cells

Example:
```python
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    # ... 7 more rows
]
```

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

Or run tests with unittest:

```bash
python -m unittest discover tests/
```

Run tests with coverage:

```bash
python -m pytest tests/ --cov=sudoku_validator --cov-report=html
```

## Examples

### Valid Complete Board

```python
valid_board = [
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

validator = SudokuValidator()
print(validator.solve_status(valid_board))  # Output: 'solved'
```

### Invalid Board (Duplicate in Row)

```python
invalid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 1],  # Two 1s in first row
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    # ... rest of the board
]

validator = SudokuValidator()
print(validator.is_valid_board(invalid_board))  # Output: False
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by [Your Name]

## Version History

- **1.0.0** - Initial release with basic validation functionality
